from utils import jumlah_harga, ubah_list, hitung_pajak

harga_barang = ubah_list("20000 40000")
total_semua = jumlah_harga(harga_barang)
pajak = hitung_pajak(total_semua)

print("Total harga:", total_semua)
print("Pajak:", pajak)
print("Total bayar:", total_semua + pajak)