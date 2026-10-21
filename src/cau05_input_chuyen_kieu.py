# 17
ma_may = input("Nhap ma may: ")
print("Kieu ma_may:", type(ma_may))

cong_suat_str = input("Nhap cong suat (W): ")
print("Kieu cong_suat_str:", type(cong_suat_str))

so_phut_str = input("Nhap so phut su dung: ")
print("Kieu so_phut_str:", type(so_phut_str))

don_gia_str = input("Nhap don gia (VND/kWh): ")
print("Kieu don_gia_str:", type(don_gia_str))

# 18: Chuyen doi kieu du lieu
cong_suat_w = float(cong_suat_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_str)

# 19: Tinh lai dien nang va chi phi sau khi chuyen kieu
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n--- KET QUA SAU KHI CHUYEN KIEU ---")
print("Dien nang (kWh):", dien_nang_kwh)
print("Chi phi (VND):", chi_phi)