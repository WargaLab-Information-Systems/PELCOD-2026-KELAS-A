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

# jawab

nama_pembeli = str(input("Nama Pembeli: "))
harga_barang = int(input("Harga Barang: "))
jumlah_barang = int(input("Jumlah Barang: "))

total_harga = harga_barang * jumlah_barang

# diskon

diskon = total_harga * 0.10


if total_harga >= 100000:
    diskon = total_harga * 0.10
    persen_diskon = 10
    print("Mendapat diskon 10%")
else:
    diskon = 0 
    persen_diskon = 0 
    print("Tidak Mendapat Diskon")


total_bayar = total_harga - diskon

# hasil

print("Hasil Pembelian")
print("Nama Pembeli", nama_pembeli)
print("Total Harga", total_harga)
print("Diskon", persen_diskon, "%")
print("Total Bayar: Rp", total_bayar)