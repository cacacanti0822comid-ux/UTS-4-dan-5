from utils import cari_nilai_tertinggi_dan_terendah, parse

def main():
    teks_input = input("Masukkan nilai: ")
    angka_list = parse(teks_input)
    nilai_maks, nilai_min = cari_nilai_tertinggi_dan_terendah(angka_list)

    print(f"Nilai maksimum: {nilai_maks}")
    print(f"Nilai minimum: {nilai_min}")

if __name__ == "__main__":
    main()