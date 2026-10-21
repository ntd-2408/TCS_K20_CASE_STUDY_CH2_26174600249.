cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# Tinh dien nang tieu thu (kWh) va chi phi (VND)
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# In gia tri va kieu du lieu cua hai ket qua
print("Dien nang (kWh):", dien_nang_kwh, "| Kieu:", type(dien_nang_kwh))
print("Chi phi (VND):", chi_phi, "| Kieu:", type(chi_phi))

# Thay so_phut bang 60 roi tinh lai
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n--- Khi thay so_phut = 60 ---")
print("Dien nang moi (kWh):", dien_nang_kwh)
print("Chi phi moi (VND):", chi_phi)