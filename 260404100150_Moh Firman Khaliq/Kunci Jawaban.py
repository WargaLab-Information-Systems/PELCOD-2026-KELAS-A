# Studi Kasus : Berbelanja di Supermarket

# Buat program yang bersifat dinamis dengan input :

# Nama pembeli
nama_pembeli = input("Masukkan nama pembeli: ")
# Harga barang
harga_barang = float(input("Masukkan harga barang: "))
# Jumlah barang
jumlah_barang = int(input("Masukkan jumlah barang:"))
# Hitung total harga (harga barang x jumlah barang)
total_harga = harga_barang * jumlah_barang

# Diskon:
# Jika total harga >= 100.000, maka akan mendapatkan diskon sebesar 10%
if total_harga >= 100000:
    diskon = 0.1 * total_harga
# Jika total harga < 100.000, maka tidak akan mendapatkan diskon
if total_harga < 100000:
    diskon = 0

# Hitung nominal diskon:
# hitung diskon (Rp) = Harga Asli x Diskon (%)
# Rumus:
# Diskon (Rp)	= Harga Asli x Diskon (%)
diskon = 0.1 if total_harga >= 100000 else 0
nominal_diskon = total_harga * diskon

# Hitung total bayar:
# Rumus:
# Total Bayar	= Harga Asli - Diskon (Rp)
total_bayar = total_harga - nominal_diskon

# Pada hasil akhir, tampilkan:
# Nama pembeli
print("Nama pembeli:", nama_pembeli)
# Total harga
print("Total harga: Rp", total_harga)
# Diskon (jika tidak ada diskon, tampilkan 0%)
print("Diskon:", diskon * 100, "%")
# Total bayar (total harga setelah diskon)
print("Total bayar: Rp", total_bayar)
