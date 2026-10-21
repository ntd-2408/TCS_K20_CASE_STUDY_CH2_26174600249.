ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))  # Ep kieu float
so_phut = int(input("Nhap so phut: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")


# Ten tep: src/cau07_chan_doan_loi.py
# So dong loi: Dong 5
# Loai loi: TypeError
# Thong bao loi: unsupported operand type(s) for /: 'str' and 'int'
# Nguyen nhan: Bien cong_suat_w chua duoc chuyen kieu sang float (van la str) nen phep chia / voi 60 bi loi.