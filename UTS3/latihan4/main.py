from utils import hitung_diskon

harga = list(map(int, input("Masukkan harga : ").split()))
total = sum(harga)
print("Total bayar setelah diskon:", total - hitung_diskon(total))