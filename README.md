# Blog với chức năng bình luận

## Thông tin cá nhân
- Họ và tên: Ngô Trường Định
- MSSV: 22641171
- STT: 81

## Mô tả dự án
Ứng dụng blog đơn giản được xây dựng bằng Flask với các chức năng cơ bản như đăng ký, đăng nhập, đăng bài và bình luận.

## Layout
Dự án sử dụng layout Single Column (Một Cột) với các đặc điểm:
- Nội dung được sắp xếp theo một cột dọc
- Sidebar cố định ở bên trái
- Các bài viết được hiển thị theo thứ tự từ trên xuống
- Responsive design cho các thiết bị di động

## Tính năng

### Phân quyền người dùng
- Actor: Có thể đăng bài viết và bình luận
- User: Chỉ có thể bình luận
- Chưa đăng nhập: Chỉ có thể xem bài viết

### Quản lý bài viết
- Đăng bài viết mới (chỉ Actor)
- Xem danh sách bài viết
- Xem chi tiết bài viết
- Bình luận trên bài viết

### Quản lý tài khoản
- Đăng ký tài khoản mới
- Đăng nhập/Đăng xuất
- Xem thông tin cá nhân

### Dashboard
- Hiển thị thống kê tổng quan về blog:
  - Số lượng bài viết đã đăng
  - Số lượng bình luận trên toàn bộ blog
  - Số lượng người dùng đã đăng ký
  - Số lượng Actor và User
- Hiển thị các bài viết mới nhất:
  - Tiêu đề bài viết
  - Tác giả
  - Ngày đăng
  - Số lượng bình luận
- Hiển thị các bình luận mới nhất:
  - Nội dung bình luận
  - Bài viết được bình luận
  - Người bình luận
  - Thời gian bình luận
- Biểu đồ thống kê:
  - Biểu đồ số lượng bài viết theo tháng
  - Biểu đồ số lượng bình luận theo tháng
  - Biểu đồ phân bố người dùng theo vai trò

## Cài đặt

### Cách 1: Sử dụng Git
```bash
# Clone repository
git clone https://github.com/ngodinhtruong/ptud-gk-de-1.git
cd ptud-gk-de-1

# Pull các thay đổi mới nhất
git pull origin main

# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường ảo
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Cài đặt các thư viện
pip install -r requirements.txt

# Chạy ứng dụng
python app.py
```

### Cách 2: Sử dụng file setup.bat (Windows)
1. Tải repository về máy
2. Chạy file `setup.bat`
3. Đợi quá trình cài đặt hoàn tất
4. Truy cập ứng dụng tại http://localhost:5000

## Tài khoản mẫu

### Actor
- Username: actor1
- Password: actor123
- Role: actor

- Username: actor2
- Password: actor123
- Role: actor

### User
- Username: user1
- Password: user123
- Role: user

- Username: user2
- Password: user123
- Role: user

## Cấu trúc thư mục
```
ptud-gk-de-1/
├── app.py              # File chính của ứng dụng
├── requirements.txt    # Danh sách các thư viện cần thiết
├── setup.bat          # Script cài đặt tự động (Windows)
├── static/            # Thư mục chứa file tĩnh
│   ├── css/          # File CSS
│   └── images/       # Hình ảnh
├── templates/         # Thư mục chứa template HTML
│   ├── base.html     # Template cơ sở
│   ├── index.html    # Trang chủ
│   ├── login.html    # Trang đăng nhập
│   ├── register.html # Trang đăng ký
│   ├── new_blog.html # Trang tạo bài viết mới
│   ├── blog_detail.html # Trang chi tiết bài viết
│   └── dashboard.html # Trang dashboard
└── blog.db           # Database SQLite
```

## Công nghệ sử dụng

### Backend
- Flask (Python web framework)
- SQLite (Database)
- Flask-Login (Xác thực người dùng)
- Flask-WTF (Form handling)

### Frontend
- Bootstrap 5
- Font Awesome
- HTML5/CSS3
- JavaScript


