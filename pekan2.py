# study case no 1
kode_kategori = input("Masukkan Kode Kategori :")
harga_produk = int(input("Masukkan Harga Produk : "))

# Menentukan kategori produk
match kode_kategori[0]:
    case 'E':
        kategori = "Elektronik"
    case 'P':
        kategori = "Pakaian"
    case 'F':
        kategori = "Perabot"
    case _:
        kategori = "Kategori tidak dikenali"

# Menentukan diskon
diskon = 0

if kategori == "Elektronik":
    diskon = 0.2 if harga_produk > 1000000 else 0
elif kategori == "Pakaian":
    diskon = 0.1 if harga_produk > 500000 else 0
elif kategori == "Perabot":
    diskon = 0.15 if harga_produk > 750000 else 0.05

# Menghitung harga akhir setelah diskon
harga_akhir = harga_produk - (harga_produk * diskon)

# Menampilkan hasil
print(f"Kategori Produk: {kategori}")
print(f"Diskon: {diskon * 100}%")
print(f"Harga Akhir Setelah Diskon: {harga_akhir}")


# Study Case no 2
penilaian = int(input("Masukkan Penilaian :"))
tahun_pengalaman = int(input("Masukkan Tahun Pengalaman (dalam Bentuk Angka) :"))
jenis_pekerjaan = input("Masukkan Jenis Pekerjaan :")
gaji = int(input("Masukkan Gaji (dalam Bentuk Angka) :"))

# Menentukan kategori penilaian
match penilaian:
    case p if p >= 90:
        kategori_penilaian = "Sangat Baik"
    case p if p >= 70:
        kategori_penilaian = "Baik"
    case p if p >= 50:
        kategori_penilaian = "Cukup"
    case _:
        kategori_penilaian = "Kurang"

# Menentukan bonus
bonus = 0

if kategori_penilaian == "Sangat Baik":
    bonus = 0.2 if tahun_pengalaman >= 5 else 0.15
elif kategori_penilaian == "Baik":
    bonus = 0.1 if jenis_pekerjaan == "Manager" else 0.05
elif kategori_penilaian == "Cukup":
    bonus = 0.05 if tahun_pengalaman >= 5 else 0
else:
    bonus = 0

# Menghitung total gaji setelah bonus
total_gaji = gaji + (gaji * bonus)

# Menampilkan hasil
print(f"Kategori Penilaian: {kategori_penilaian}")
print(f"Bonus: {bonus * 100}%")
print(f"Total Gaji Setelah Bonus: {total_gaji}")



