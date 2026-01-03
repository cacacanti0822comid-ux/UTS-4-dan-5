from utils import jumlah_data, ubah_ke_list, ambil_desimal

masukan_teks = input("Masukkan angka desimal: ")
list_angka = ubah_ke_list(masukan_teks)

desimal_diambil = int(input("Ingin berapa angka di belakang koma? "))

total_semua = jumlah_data(list_angka)
hasil_format = ambil_desimal(total_semua, desimal_diambil)

print("Total angka:", total_semua)
print("Hasil format:", hasil_format)