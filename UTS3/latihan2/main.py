from utils import hitung_total, ubah_teks_ke_angka

def main():
    
    masukan = input("Masukkan deret angka (pisahkan dengan spasi): ")
    
    deret_angka = ubah_teks_ke_angka(masukan)
    
    total = hitung_total(deret_angka)
    
    print("Deret angka:", deret_angka)
    print("Total jumlah:", total)

if __name__ == "__main__":
    main()