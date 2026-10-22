# Bài 10: Chương trình tích hợp cuối Case Study
from datetime import datetime

ma_phien = input("Mã phiên: ")
ma_may = input("Máy: ")
cong_suat_w = float(input("Công suất thiết bị (W): "))
so_phut = int(input("Thời gian sử dụng (phút): "))
don_gia_kwh = float(input("Đơn giá điện (VND/kWh): "))

# Tính toán
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
su_dung_tren_60 = so_phut > 60
ghi_nhan_luc = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Xuất kết quả theo định dạng yêu cầu
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {so_phut} phút")
print(f"Điện năng: {dien_nang_kwh} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {su_dung_tren_60}")
print(f"Ghi nhận lúc: {ghi_nhan_luc}")