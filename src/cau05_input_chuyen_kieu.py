# Bài 5: Nhập dữ liệu và chuyển đổi kiểu
ma_may = input("Nhập mã máy: ")
cong_suat_w = input("Nhập công suất W: ")
so_phut = input("Nhập số phút: ")
don_gia_kwh = input("Nhập đơn giá điện/kWh: ")

# In type ngay sau khi nhập (tất cả đều là str)
print(type(ma_may), type(cong_suat_w), type(so_phut), type(don_gia_kwh))

# Chuyển đổi kiểu dữ liệu theo yêu cầu
cong_suat_w = float(cong_suat_w)
so_phut = int(so_phut)
don_gia_kwh = float(don_gia_kwh)

# Tính lại điện năng và chi phí sau khi chuyển kiểu
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print(f"Điện năng tính lại: {dien_nang_kwh} kWh")
print(f"Chi phí tính lại: {chi_phi} VND")