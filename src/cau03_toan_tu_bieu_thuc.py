tong_phut = 135
cong_suat_w = 250

# Tinh so gio tron ven va so phut con lai
so_gio = tong_phut // 60
so_phut_du = tong_phut % 60
print("So gio tron ven:", so_gio, "gio, so phut con lai:", so_phut_du, "phut")

# Bien su_dung_lau nhan True khi tong_phut > 60
su_dung_lau = tong_phut > 60
print("Su dung lau (>60 phut):", su_dung_lau)

# Bien du_lieu_hop_le nhan True khi cong_suat_w > 0 va tong_phut > 0
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Du lieu hop le:", du_lieu_hop_le)

# Du doan roi kiem chung hai bieu thuc
print("Ket qua 100 + 20 * 3 =", 100 + 20 * 3)
print("Ket qua (100 + 20) * 3 =", (100 + 20) * 3)