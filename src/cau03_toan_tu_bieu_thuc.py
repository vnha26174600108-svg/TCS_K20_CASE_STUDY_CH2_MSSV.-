# Bài 3: Toán tử và biểu thức
tong_phut = 135
cong_suat_w = 250

# 9. Dùng // và % để tính số giờ trọn vẹn và số phút còn lại
so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print(f"Số giờ: {so_gio}, Số phút còn lại: {so_phut_con_lai}")

# 10. Tạo bien su_dung_lau nhận True khi tong_phut > 60
su_dung_lau = tong_phut > 60
print("Sử dụng lâu:", su_dung_lau)

# 11. Tạo bien du_lieu_hop_le nhận True khi cong_suat_w > 0 và tong_phut > 0
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Dữ liệu hợp lệ:", du_lieu_hop_le)

# 12. Dự đoán rồi kiểm chứng hai biểu thức toán học
print("100 + 20 * 3 =", 100 + 20 * 3)
print("(100 + 20) * 3 =", (100 + 20) * 3)