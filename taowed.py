import requests

# Thông tin cần thiết
access_token = 'EAAdByNRkf5IBOxNBmQoJmpchciB6FVq0dwTr6fr54bMsYXGEW8tegkwhtfoItpb1DOGXSVAmgyaLWCcmVyW8Cuy3mj9Q46bR0y6AHBWQZA2Jni707mIsmTdy2kPdcnIDelsSHZChKxH9Urev8EGUaka7zMqXaHx4d38oY4Kj1ZCc5Mkzt9M1fZCpznul5qYdpBPqfePWIgqeWxrZBZAh5O'  # Thay bằng access token của bạn
page_id = '566595959881091'            # Thay bằng ID của trang bạn quản lý
message = 'Đây là bài viết tự động từ Python của Tra MY'  # Nội dung bài đăng

# URL API của Facebook để đăng bài
url = f'https://graph.facebook.com/{page_id}/feed'

# Dữ liệu gửi đi
payload = {
    'message': message,
    'access_token': access_token
}

# Gửi yêu cầu POST đến Facebook Graph API
response = requests.post(url, data=payload)

# Xử lý kết quả
if response.status_code == 200:
    print("✅ Đăng bài thành công!")
    print("ID bài viết:", response.json().get('id'))
else:
    print("❌ Lỗi khi đăng bài:")
    print(response.status_code)
    print(response.text)