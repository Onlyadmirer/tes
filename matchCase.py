penilaian = int(input("Masukkan penilaian :"))
pengalaman = int(input("Masukkan pengalaman kerja (tahun) :"))
jenisPekerjaan = input("masukkan jenis pekerjaan : ")
gaji = int(input("masukkan gaji : "))

match penilaian:
    case p if p >= 90:
        kategoriPenilaiaan = "sangat baik"
    case p if 70 <= p < 90:
        kategoriPenilaiaan = "baik"
    case p if 50 <= p < 70:
        kategoriPenilaiaan = "cukup"
    case p if p < 50:
        kategoriPenilaiaan = "kurang"
    case _:
        kategoriPenilaiaan = "tidak terdefinisi"
        
if kategoriPenilaiaan == "sangat baik":
    bonus = 0.2 if pengalaman >= 5 else 0.1
elif kategoriPenilaiaan == "baik":
    bonus = 0.1 if jenisPekerjaan == "manager" else 0.05
elif kategoriPenilaiaan == "cukup":
    bonus = 0.05 if pengalaman >= 5 else 0
else:
    bonus = "tidak ada bonus"
    
gajiDenganBonus = gaji * (1 + bonus)

print(f"kategori penilaiaan : {kategoriPenilaiaan}")
print(f"bonus : {bonus * 100}%")
print(f"total gaji setelah bonus : {gajiDenganBonus:.2f}")