# Bài 7: Chẩn đoán và sửa lỗi
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))  # Đã sửa: bọc float() vì input() mặc định là str
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000

print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")  # Đã sửa: bổ sung dấu ngoặc nhọn } bị thiếu ở cuối f-string

# --- BÁO CÁO LỖI ---
# Lỗi 1: TypeError do 'cong_suat_w' là kiểu chuỗi (str) nhân với số (int/float) bị lỗi kiểu dữ liệu.
# Lỗi 2: SyntaxError do thiếu dấu đóng ngoặc nhọn '}' ở dòng lệnh in f-string cuối cùng.