nilai_mahasiswa = [55, 78, 82, 67, 90, 58, 74]
jumlah_lebih_70 = 0
total_nilai = 0

for i in nilai_mahasiswa:
    if i > 70:
        jumlah_lebih_70 =+ 1
        print(i)
        
for i in nilai_mahasiswa:
    total_nilai += i
    
rata = total_nilai / len(nilai_mahasiswa)
print(f"rata-rata = {rata}")



