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

Nama = input("masukkan nama pembeli:")
harga_barang = int(input("harga barang:"))
jumlah_barang = int(input("jumlah barang:"))
total_harga = harga_barang * jumlah_barang

nilai = int(total_harga)
if nilai >= (100000):
    diskon = total_harga * 0.1
    total_bayar = total_harga - diskon
    print("total_harga:", total_harga)
    print("diskon:", diskon)
    print("total_bayar:", total_bayar)
else :
    diskon = 0
    total_bayar = total_harga - diskon
    print("total_harga:", total_harga)
    print("diskon:", diskon)
    print("total_bayar:", total_bayar)
    print("tidak ada diskon")

    
