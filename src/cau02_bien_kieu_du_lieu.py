# Bài 2: Biến và kiểu dữ liệu
ma_phien = "LAB026"
ma_may = "PC12"
cong_suat_w = 250.0
thoi_gian = 90
trang_thai = True
ghi_chu = None

# In từng giá trị và dùng type() để kiểm tra kiểu dữ liệu
print(ma_phien, type(ma_phien))
print(ma_may, type(ma_may))
print(cong_suat_w, type(cong_suat_w))
print(thoi_gian, type(thoi_gian))
print(trang_thai, type(trang_thai))
print(ghi_chu, type(ghi_chu))

# Thay đổi thời gian sử dụng từ 90 thành 120 bằng phép gán lại và in giá trị mới
thoi_gian = 120
print("Thời gian mới:", thoi_gian, type(thoi_gian))