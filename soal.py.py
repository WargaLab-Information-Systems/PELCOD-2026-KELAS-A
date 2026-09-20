# Studi Kasus : Berbelanja di Supermarket

# Buat program yang bersifat dinamis dengan input :

# Nama pembeli
# Harga barang
# Jumlah barang
# Hitung total harga (harga barang x jumlah barang)

# Diskon:
# Jika total harga >= 100.000, maka akan mendapatkan diskon sebesar 10%
# Jika total harga < 100.000, maka tidak akan mendapatkan diskon

# Hitung nominal diskon:
# Rumus:
# Diskon (Rp)	= Harga Asli x Diskon (%)

# Hitung total bayar:
# Rumus:
# Total Bayar	= Harga Asli - Diskon (Rp)

# Pada hasil akhir, tampilkan:
# Nama pembeli
# Total harga
# Diskon (jika tidak ada diskon, tampilkan 0%)
# Total bayar (total harga setelah diskon)


# ==== Berbelanja di Supermarket ====
nama_pembeli = input("Nama pembeli: ")
harga_barang = float(input("Jumlah barang: Rp"))
jumlah_barang = int(input("Jumlah barang: "))
total_harga = harga_barang * jumlah_barang

# ==== Diskon ====
if total_harga >= 100.000,:
    diskon_persen = 10
else:
    diskon_persen = 0

# ==== Hitung nominal diskon ====
diskon = total_harga * diskon_persen / 100

# ==== Hitung total bayar ====
total_bayar = harga_barang - diskon

# ==== Hasil akhir, tampilkan: ====
print ("Nama pembeli")
print ("Total harga")
print ("Diskon")
print ("Total bayar")
