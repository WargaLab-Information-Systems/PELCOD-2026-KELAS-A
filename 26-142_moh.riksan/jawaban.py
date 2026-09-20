# Study Kasus : Berbelanja di supermarket 

#Input
nama_pembeli = "Moh.Riksan"
harga_barang = 30000
jumlah_barang = 6
# Hitung total harga 
total_harga = harga_barang * jumlah_barang

# Menentukan diskon
if total_harga >= 100000:
    diskon_persen = 10
else:
    diskon_persen = 0

# Hitung total diskon dan total bayar
diskon_rupiah = total_harga * diskon_persen / 100
total_bayar = total_harga - diskon_rupiah

# Tampilkan hasil
print("\n==== Struk Belanja ====")
print(f"Nama Pembeli: {nama_pembeli}")
print(f"Total Harga: {total_harga}")
print(f"Diskon: {diskon_persen}%")
print(f"Total Bayar: {total_bayar}")
