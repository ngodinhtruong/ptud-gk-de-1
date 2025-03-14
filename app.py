from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False, default='user')  # 'actor' hoặc 'user'
    blogs = db.relationship('Blog', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_actor(self):
        return self.role == 'actor'

    def is_user(self):
        return self.role == 'user'

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='blog', lazy=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
@login_required
def index():
    blogs = Blog.query.order_by(Blog.created_at.desc()).all()
    return render_template('index.html', blogs=blogs)

@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role', 'user')  # Mặc định là user

        if User.query.filter_by(username=username).first():
            flash('Tên đăng nhập đã tồn tại!', 'danger')
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash('Email đã được sử dụng!', 'danger')
            return redirect(url_for('register'))

        user = User(username=username, email=email, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash('Đăng ký thành công! Vui lòng đăng nhập.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Đăng nhập thành công!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Tên đăng nhập hoặc mật khẩu không chính xác!', 'danger')

    return render_template('signin.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Đã đăng xuất thành công!', 'success')
    return redirect(url_for('login'))

@app.route('/blog/new', methods=['GET', 'POST'])
@login_required
def new_blog():
    if not current_user.is_actor():
        flash('Chỉ actor mới có quyền tạo bài viết!', 'danger')
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        if not title or not content:
            flash('Vui lòng điền đầy đủ thông tin!', 'danger')
            return redirect(url_for('new_blog'))

        # Tạo URL ảnh ngẫu nhiên từ Picsum
        image_url = f"https://picsum.photos/seed/{datetime.now().timestamp()}/800/400"

        blog = Blog(
            title=title,
            content=content,
            image_url=image_url,
            user_id=current_user.id
        )
        db.session.add(blog)
        db.session.commit()

        flash('Bài viết đã được tạo thành công!', 'success')
        return redirect(url_for('blog_detail', blog_id=blog.id))

    return render_template('new_blog.html')

@app.route('/blog/<int:blog_id>')
@login_required
def blog_detail(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    return render_template('blog_detail.html', blog=blog)

@app.route('/blog/<int:blog_id>/comment', methods=['POST'])
@login_required
def add_comment(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    content = request.form.get('content')

    if not content:
        flash('Vui lòng nhập nội dung bình luận!', 'danger')
        return redirect(url_for('blog_detail', blog_id=blog_id))

    # Kiểm tra xem người dùng có phải là tác giả của bài viết không
    if current_user.id == blog.user_id:
        flash('Bạn không thể bình luận vào bài viết của chính mình!', 'warning')
        return redirect(url_for('blog_detail', blog_id=blog_id))

    # Tạo bình luận mới
    comment = Comment(
        content=content,
        user_id=current_user.id,
        blog_id=blog_id
    )
    db.session.add(comment)
    db.session.commit()

    # Thông báo khác nhau cho actor và user
    if current_user.is_actor():
        flash('Bình luận của bạn đã được thêm thành công!', 'success')
    else:
        flash('Cảm ơn bạn đã bình luận!', 'success')

    return redirect(url_for('blog_detail', blog_id=blog_id))

@app.route('/blog/<int:blog_id>/delete/<int:comment_id>')
@login_required
def delete_comment(blog_id, comment_id):
    blog = Blog.query.get_or_404(blog_id)
    comment = Comment.query.get_or_404(comment_id)

    # Chỉ cho phép tác giả bài viết hoặc tác giả bình luận xóa bình luận
    if current_user.id != blog.user_id and current_user.id != comment.user_id:
        flash('Bạn không có quyền xóa bình luận này!', 'danger')
        return redirect(url_for('blog_detail', blog_id=blog_id))

    db.session.delete(comment)
    db.session.commit()
    flash('Bình luận đã được xóa!', 'success')
    return redirect(url_for('blog_detail', blog_id=blog_id))

@app.route('/blog/<int:blog_id>/edit/<int:comment_id>', methods=['GET', 'POST'])
@login_required
def edit_comment(blog_id, comment_id):
    blog = Blog.query.get_or_404(blog_id)
    comment = Comment.query.get_or_404(comment_id)

    # Chỉ cho phép tác giả bình luận sửa bình luận của mình
    if current_user.id != comment.user_id:
        flash('Bạn không có quyền sửa bình luận này!', 'danger')
        return redirect(url_for('blog_detail', blog_id=blog_id))

    if request.method == 'POST':
        content = request.form.get('content')
        if not content:
            flash('Vui lòng nhập nội dung bình luận!', 'danger')
            return redirect(url_for('edit_comment', blog_id=blog_id, comment_id=comment_id))

        comment.content = content
        db.session.commit()
        flash('Bình luận đã được cập nhật!', 'success')
        return redirect(url_for('blog_detail', blog_id=blog_id))

    return render_template('edit_comment.html', blog=blog, comment=comment)

@app.route('/user/<int:user_id>')
@login_required
def user_profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user.html', user=user)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Tạo các tài khoản mẫu với vai trò actor và user
        users = [
            {'username': 'actor1', 'email': 'actor1@example.com', 'password': 'actor123', 'role': 'actor'},
            {'username': 'actor2', 'email': 'actor2@example.com', 'password': 'actor123', 'role': 'actor'},
            {'username': 'user1', 'email': 'user1@example.com', 'password': 'user123', 'role': 'user'},
            {'username': 'user2', 'email': 'user2@example.com', 'password': 'user123', 'role': 'user'}
        ]

        for user_data in users:
            user = User.query.filter_by(username=user_data['username']).first()
            if not user:
                user = User(
                    username=user_data['username'],
                    email=user_data['email'],
                    role=user_data['role']
                )
                user.set_password(user_data['password'])
                db.session.add(user)
        
        db.session.commit()
    app.run(debug=True) 