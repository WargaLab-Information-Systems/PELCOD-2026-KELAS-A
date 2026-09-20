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



nama = input("nama pembeli: ")
harga = int(input("harga barang: " ))
jumlah = int(input("jumlah barang: "))
total = harga * jumlah

if total >= 100.000:
    diskon = total * 10/100
    harga_bayar = total - diskon
    print("total harga setelah diskon", harga_bayar)
else:
    diskon = 0
    harga_bayar = total - diskon
    print("total harga bayar", harga_bayar)

print("Untuk", nama, "total harga yang harus di bayar", total,"total diskon yang di dapat", diskon, "total harga yang di bayar", harga_bayar)

 

