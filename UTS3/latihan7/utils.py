def jumlah_data(kumpulan_angka):
    return sum(kumpulan_angka)

def ubah_ke_list(teks_mentah):
    return list(map(float, teks_mentah.replace(",", ".").split()))

def ambil_desimal(nilai_asli, banyak_desimal):
    pola_format = "{:." + str(banyak_desimal) + "f}"
    return pola_format.format(nilai_asli)