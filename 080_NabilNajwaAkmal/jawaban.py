nama = "nabil"
harga = 700
jumlahbarang = 10
totalharga = harga * jumlahbarang

if totalharga >= 500:
    persentase_diskon = 0.10
else:
    persentase_diskon = 0.0

#menghitung diskon rp
diskon_rp = totalharga * persentase_diskon

#menghitung total bayar
total_bayar = totalharga - diskon_rp

print("Nama pembeli :", nama)
print("Total harga diskon :", totalharga)
print("Diskon (Rp) :", diskon_rp)
print("Total bayar :", total_bayar)