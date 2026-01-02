import os
from fungsi_bangun_datar import (
    persegi, persegi_panjang, segitiga, jajar_genjang,
    layang_layang, belah_ketupat, trapesium,
    lingkaran, heksagon, pentagon
)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_menu():
    clear()
    print("=== Program Hitung Keliling dan Luas Bangun Datar ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Jajar Genjang")
    print("5. Layang-Layang")
    print("6. Belah Ketupat")
    print("7. Trapesium")
    print("8. Lingkaran")
    print("9. Heksagon")
    print("10. Pentagon")
    print("11. Keluar")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih bangun datar (1-11): ").strip()

        if pilihan == "11":
            print("Program selesai. Terima kasih!")
            break

        try:
            if pilihan == "1":
                s = float(input("Masukkan sisi: "))
                kel, area = persegi(s)
            elif pilihan == "2":
                p = float(input("Masukkan panjang: "))
                w = float(input("Masukkan lebar: "))
                kel, area = persegi_panjang(p, w)
            elif pilihan == "3":
                a = float(input("Masukkan alas: "))
                t = float(input("Masukkan tinggi: "))
                x = float(input("Masukkan sisi x: "))
                y = float(input("Masukkan sisi y: "))
                z = float(input("Masukkan sisi z: "))
                kel, area = segitiga(a, t, x, y, z)
            elif pilihan == "4":
                a = float(input("Masukkan alas: "))
                t = float(input("Masukkan tinggi: "))
                m = float(input("Masukkan sisi miring: "))
                kel, area = jajar_genjang(a, t, m)
            elif pilihan == "5":
                d1 = float(input("Masukkan diagonal 1: "))
                d2 = float(input("Masukkan diagonal 2: "))
                u = float(input("Masukkan sisi u: "))
                v = float(input("Masukkan sisi v: "))
                kel, area = layang_layang(d1, d2, u, v)
            elif pilihan == "6":
                d1 = float(input("Masukkan diagonal 1: "))
                d2 = float(input("Masukkan diagonal 2: "))
                s = float(input("Masukkan sisi: "))
                kel, area = belah_ketupat(d1, d2, s)
            elif pilihan == "7":
                a = float(input("Masukkan sisi atas: "))
                b = float(input("Masukkan sisi bawah: "))
                t = float(input("Masukkan tinggi: "))
                u = float(input("Masukkan sisi u: "))
                v = float(input("Masukkan sisi v: "))
                kel, area = trapesium(a, b, t, u, v)
            elif pilihan == "8":
                r = float(input("Masukkan jari-jari: "))
                kel, area = lingkaran(r)
            elif pilihan == "9":
                s = float(input("Masukkan sisi: "))
                kel, area = heksagon(s)
            elif pilihan == "10":
                s = float(input("Masukkan sisi: "))
                kel, area = pentagon(s)
            else:
                continue
        except ValueError:
            continue

        print(f"\nKeliling = {kel}")
        print(f"Luas = {area}")

        # cukup Enter untuk lanjut ke menu berikutnya
        input("\n")
        # loop akan otomatis menampilkan menu lagi

if __name__ == "__main__":
    main()