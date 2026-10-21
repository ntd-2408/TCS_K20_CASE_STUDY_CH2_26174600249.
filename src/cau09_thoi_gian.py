from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))

# ket qua phep tru (ket_thuc - bat_dau) la 1:50:00 (1 gio 50 phut).
# giai thich su khac nhau:
#   - datetime: Doi tuong mieu ta moc thoi gian cu the (nam, thang, ngay, gio, phut, giay).
#   - str: Chuoi van ban bieu dien thoi gian (dang text).
#   - timedelta: Doi tuong bieu thi khoang thoi gian / do lech giua 2 moc datetime.
