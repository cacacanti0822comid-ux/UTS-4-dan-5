def cari_nilai_tertinggi_dan_terendah(angka_list):
    nilai_maks = max(angka_list)
    nilai_min = min(angka_list)
    return nilai_maks, nilai_min

def parse(teks_input):
    return [int(elemen) for elemen in teks_input.split()]