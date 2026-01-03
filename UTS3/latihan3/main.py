from utils import hitung_rata_rata, cek_kelulusan, parse_input

def main():
    
    masukan_nilai = input("Masukkan nilai siswa (pisahkan dengan spasi): ")
    nilai_siswa = parse_input(masukan_nilai)

    rata2 = hitung_rata_rata(nilai_siswa)
    print("Rata-rata:", rata2)

    batas = float(input("Masukkan batas kelulusan: "))

    status = cek_kelulusan(rata2, batas)

    print("Status:", status)

if __name__ == "__main__":
    main()