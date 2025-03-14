@echo off
echo ====================================
echo    Install Blog Application
echo    Author: Ngo Truong Dinh - 22641171 - stt: 81
echo ====================================
echo.

:: Kiểm tra Python đã được cài đặt chưa
python --version >nul 2>&1
if errorlevel 1 (
    echo Python chua duoc cai dat! Vui long cai dat Python 3.8 hoac cao hon.
    echo Tai Python tai: https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Tạo môi trường ảo
echo Dang tao moi truong ao...
python -m venv venv
if errorlevel 1 (
    echo Khong the tao moi truong ao!
    pause
    exit /b 1
)

:: Kích hoạt môi trường ảo
echo Dang kich hoat moi truong ao...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo Khong the kich hoat moi truong ao!
    pause
    exit /b 1
)

:: Cài đặt các thư viện cần thiết
echo Dang cai dat cac thu vien...
pip install -r requirements.txt
if errorlevel 1 (
    echo Khong the cai dat cac thu vien!
    pause
    exit /b 1
)

:: Tạo thư mục static nếu chưa tồn tại
if not exist "static" mkdir static
if not exist "static\css" mkdir static\css
if not exist "static\images" mkdir static\images

:: Tạo thư mục templates nếu chưa tồn tại
if not exist "templates" mkdir templates

:: Xóa file database cũ nếu có
if exist "blog.db" del blog.db

:: Chạy ứng dụng
echo.
echo ====================================
echo    Cai dat thanh cong!
echo    Dang khoi dong ung dung...
echo ====================================
echo.
echo Ung dung se chay tai: http://localhost:5000
echo Nhan Ctrl+C de dung ung dung
echo.
python app.py

:: Khi người dùng nhấn Ctrl+C, thoát môi trường ảo
deactivate 