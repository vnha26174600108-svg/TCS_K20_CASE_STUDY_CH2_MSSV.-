# Bài 4: Tính điện năng và chi phí
cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# Công thức tính điện năng (kWh) và chi phí (VND)
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("--- Khi số phút = 90 ---")
print("Điện năng:", dien_nang_kwh, type(dien_nang_kwh))
print("Chi phí:", chi_phi, type(chi_phi))

# Thay so_phut bằng 60 rồi chạy lại và so sánh
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("--- Khi số phút = 60 ---")
print("Điện năng:", dien_nang_kwh, type(dien_nang_kwh))
print("Chi phí:", chi_phi, type(chi_phi))