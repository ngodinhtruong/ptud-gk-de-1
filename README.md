# Blog với chức năng bình luận

## Thông tin cá nhân


- Họ và tên: Ngô Trường Định
- MSSV: 22641171
- STT: 81


## Mô tả dự án

Dự án là một blog đơn giản với các chức năng:

- Đăng ký và đăng nhập người dùng
- Đăng bài viết với hình ảnh
- Bình luận trên bài viết
- Xem thông tin cá nhân và bài viết của người dùng
- Giao diện theo layout Single Column (Một Cột)

## Công nghệ sử dụng

- Backend: Python Flask
- Database: SQLite
- Frontend: HTML, CSS, Bootstrap 5
- Authentication: Flask-Login

## Hướng dẫn cài đặt

### Yêu cầu hệ thống

- Python 3.8 trở lên
- pip (Python package manager)

### Các bước cài đặt

1. Clone repository:

```bash
git clone https://github.com/[username]/ptud-gk-de-1.git
cd ptud-gk-de-1
```

2. Tạo môi trường ảo (virtual environment):

```bash
python -m venv venv
```

3. Kích hoạt môi trường ảo:

- Windows:

```bash
venv\Scripts\activate
```

- Linux/Mac:

```bash
source venv/bin/activate
```

4. Cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

5. Chạy ứng dụng:

```bash
python app.py
```

6. Truy cập ứng dụng:

- Mở trình duyệt web
- Truy cập địa chỉ: http://localhost:5000

## Tài khoản mặc định

- Admin:
  - Username: admin
  - Password: admin123

## Cấu trúc thư mục

```
ptud-gk-de-1/
├── app.py                 # File chính của ứng dụng
├── requirements.txt       # Danh sách các thư viện cần thiết
├── README.md             # File hướng dẫn
├── database/             # Thư mục chứa database
├── static/               # Thư mục chứa file tĩnh
│   ├── css/             # File CSS
│   └── js/              # File JavaScript
└── templates/           # Thư mục chứa template HTML
    ├── base.html        # Template cơ sở
    ├── index.html       # Trang chủ
    ├── signin.html      # Trang đăng nhập
    ├── signup.html      # Trang đăng ký
    ├── user.html        # Trang thông tin người dùng
    ├── blog_detail.html # Trang chi tiết bài viết
    └── new_blog.html    # Trang tạo bài viết mới
```

## Chức năng chính

1. Quản lý người dùng:

   - Đăng ký tài khoản mới
   - Đăng nhập/Đăng xuất
   - Xem thông tin cá nhân
2. Quản lý bài viết:

   - Tạo bài viết mới với hình ảnh
   - Xem danh sách bài viết
   - Xem chi tiết bài viết
3. Quản lý bình luận:

   - Thêm bình luận vào bài viết
   - Xem danh sách bình luận

## Layout

Dự án sử dụng layout Single Column (Một Cột) với các đặc điểm:

- Nội dung được sắp xếp theo một cột dọc
- Header cố định ở trên cùng
- Các bài viết được hiển thị theo thứ tự từ trên xuống
- Responsive design cho các thiết bị di động
