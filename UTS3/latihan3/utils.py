def hitung_rata_rata(nilai_list):
    return sum(nilai_list) / len(nilai_list)

def cek_kelulusan(rata_rata, batas):
    return "Lulus" if rata_rata >= batas else "Tidak Lulus"

def parse_input(teks):
    return [float(x) for x in teks.split()]