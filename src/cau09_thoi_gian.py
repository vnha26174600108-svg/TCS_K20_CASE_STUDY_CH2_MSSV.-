# Bài 9: Dữ liệu thời gian
from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau

print(thoi_luong)
print(type(thoi_luong))

# Giải thích các kiểu dữ liệu:
# - datetime: Đối tượng thời gian chứa đầy đủ thông tin ngày, giờ, phút, giây, microsecond.
# - str: Chuỗi văn bản bình thường (sau khi định dạng bằng strftime) dùng để hiển thị hoặc lưu trữ.
# - timedelta: Đối tượng biểu diễn khoảng thời gian (hiệu số giữa hai đối tượng datetime).