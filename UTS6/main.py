import os
from logika import getgradelabel  
from logika import konversi_huruf_ke_nilai
from logika import total_sks
from logika import total_nilai_ipk
from logika import hitung_ips

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  

    print("\n===== MENU UTAMA =====")
    print("1. Konversi nilai angka ke huruf")
    print("2. Konversi huruf ke nilai IPK")
    print("3. Hitung total SKS")
    print("4. Hitung total nilai IPK berbobot SKS")
    print("5. Hitung IPS (Indeks Prestasi Semester)")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\n============= NO 1 ===========")
        try:
            nilai_angka = int(input("Masukkan nilai: "))
            label = getgradelabel(nilai_angka)
            print("Label huruf:", label)
        except ValueError:
            print("Input tidak valid. Harus berupa angka bulat.")
        input("\n")

    elif pilihan == "2":
        print("\n============= NO 2 ===========")
        huruf = input("Masukkan label huruf: ")
        nilai_ipk = konversi_huruf_ke_nilai(huruf)
        if nilai_ipk is not None:
            print("Nilai IPK:", nilai_ipk)
        else:
            print("Label huruf tidak dikenali.")
        input("\n")

    elif pilihan == "3":
        print("\n============= NO 3 ===========")
        try:
            jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))
            daftar_sks = []
            for i in range(jumlah_mk):
                sks = int(input(f"Jumlah SKS mata kuliah {i+1}: "))
                daftar_sks.append(sks)
            total = total_sks(daftar_sks)
            print("Total SKS:", total)
        except ValueError:
            print("Input tidak valid. Harus berupa angka bulat.")
        input("\n")

    elif pilihan == "4":
        print("\n============= NO 4 ===========")
        jumlah = int(input("Jumlah Data: "))
        daftar_sks = []
        daftar_nilai = []
        print("------ input sks ------")
        for i in range(jumlah):
            sks = int(input(f"SKS {i+1}: "))
            daftar_sks.append(sks)
        print("\n------ Input Nilai Mahasiswa ------")
        for i in range(jumlah):
            nilai = int(input(f"Nilai {i+1}: "))
            daftar_nilai.append(nilai)
        total = total_nilai_ipk(daftar_sks, daftar_nilai)
        print("\nTotal Nilai:", round(total, 2))
        input("\n")

    elif pilihan == "5":
        print("\n============= NO 5 ===========")
        jumlah = int(input("Jumlah Data: "))
        daftar_sks = []
        daftar_nilai = []
        print("------ input sks ------")
        for i in range(jumlah):
            sks = int(input(f"SKS {i+1}: "))
            daftar_sks.append(sks)
        print("\n------ input nilai Mahasiswa ------")
        for i in range(jumlah):
            nilai = int(input(f"Nilai {i+1}: "))
            daftar_nilai.append(nilai)
        ips = hitung_ips(daftar_sks, daftar_nilai)
        print("\nIPS:", ips)
        input("\n")

    elif pilihan == "6":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih antara 0 sampai 5.")
        input("\n")