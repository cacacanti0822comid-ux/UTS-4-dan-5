import os
from fungsi_bangun_ruang import (
    kubus, balok, prisma_segitiga, limas_segitiga,
    tabung, kerucut, bola, prisma_segiempat,
    limas_segiempat, torus
)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_menu():
    clear()
    print("=== Program Hitung Volume dan Luas Permukaan Bangun Ruang ===")
    print("1. Kubus")
    print("2. Balok")
    print("3. Prisma Segitiga")
    print("4. Limas Segitiga")
    print("5. Tabung")
    print("6. Kerucut")
    print("7. Bola")
    print("8. Prisma Segiempat")
    print("9. Limas Segiempat")
    print("10. Torus")
    print("11. Keluar")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih bangun ruang (1-11): ").strip()

        if pilihan == "11":
            print("Program selesai. Terima kasih!")
            break

        try:
            if pilihan == "1":
                s = float(input("Masukkan sisi: "))
                volume, luas = kubus(s)
            elif pilihan == "2":
                p = float(input("Masukkan panjang: "))
                l = float(input("Masukkan lebar: "))
                t = float(input("Masukkan tinggi: "))
                volume, luas = balok(p, l, t)
            elif pilihan == "3":
                a = float(input("Masukkan alas segitiga: "))
                t_alas = float(input("Masukkan tinggi segitiga alas: "))
                tinggi_prisma = float(input("Masukkan tinggi prisma: "))
                sisi1 = float(input("Masukkan sisi 1 segitiga alas: "))
                sisi2 = float(input("Masukkan sisi 2 segitiga alas: "))
                sisi3 = float(input("Masukkan sisi 3 segitiga alas: "))
                volume, luas = prisma_segitiga(a, t_alas, tinggi_prisma, sisi1, sisi2, sisi3)
            elif pilihan == "4":
                a = float(input("Masukkan alas segitiga: "))
                t_alas = float(input("Masukkan tinggi segitiga alas: "))
                tinggi_limas = float(input("Masukkan tinggi limas: "))
                volume, luas = limas_segitiga(a, t_alas, tinggi_limas)
            elif pilihan == "5":
                r = float(input("Masukkan jari-jari: "))
                t = float(input("Masukkan tinggi: "))
                volume, luas = tabung(r, t)
            elif pilihan == "6":
                r = float(input("Masukkan jari-jari: "))
                t = float(input("Masukkan tinggi: "))
                volume, luas = kerucut(r, t)
            elif pilihan == "7":
                r = float(input("Masukkan jari-jari: "))
                volume, luas = bola(r)
            elif pilihan == "8":
                p = float(input("Masukkan panjang: "))
                l = float(input("Masukkan lebar: "))
                t = float(input("Masukkan tinggi: "))
                volume, luas = prisma_segiempat(p, l, t)
            elif pilihan == "9":
                p = float(input("Masukkan panjang alas: "))
                l = float(input("Masukkan lebar alas: "))
                t = float(input("Masukkan tinggi limas: "))
                volume, luas = limas_segiempat(p, l, t)
            elif pilihan == "10":
                r = float(input("Masukkan jari-jari lingkaran kecil: "))
                R = float(input("Masukkan jari-jari lingkaran besar: "))
                volume, luas = torus(r, R)
            else:
                continue
        except ValueError:
            continue

        print(f"\nVolume = {volume}")
        print(f"Luas Permukaan = {luas}")

        # cukup Enter untuk lanjut ke menu berikutnya
        input("\n")

if __name__ == "__main__":
    main()