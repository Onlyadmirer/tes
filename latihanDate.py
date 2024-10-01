import datetime as dt

print("Masukkan tanggal, bulan, dan tahun lahir anda")

tanggal = int(input("Tanggal:\t "))
bulan = int(input("Bulan :\t\t "))
tahun = int(input("Tahun :\t\t "))

lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda : {lahir}")
print(f"anda lahir pada hari {lahir:%A}")

hariIni = dt.date.today()
print(f"hari ini tanggal: {hariIni}")

umur = hariIni - lahir
# usiaTahun = umur // dt.timedelta(days=365) ; format 1
usiaTahun = umur.days // 365
print(f"umur anda adalah {usiaTahun} tahun")