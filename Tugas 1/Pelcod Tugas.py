jumlah_buku = 3
harga_buku = 15000

jumlah_pulpen = 2
harga_pulpen = 5000

total_buku = jumlah_buku * harga_buku
total_pulpen = jumlah_pulpen * harga_pulpen

total_belanja = total_buku + total_pulpen

if total_belanja > 50000:
    diskon = total_belanja * 10 / 100
else: 
    diskon = 0

total_bayar = total_belanja - diskon

print("Total belanja: Rp", total_belanja)
print("Diskon: Rp", diskon)
print("Total bayar: Rp", total_bayar)
print("barang yang dibeli:", jumlah_buku, "buku dan", jumlah_pulpen, "pulpen")