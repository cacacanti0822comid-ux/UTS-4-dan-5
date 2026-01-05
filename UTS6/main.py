import os
from logika import getgradelabel  
from logika import konversi_huruf_ke_nilai
from logika import total_sks
from logika import total_nilai_ipk
from logika import hitung_ips

print("============== NO 1 ===============")
try:
    nilai_angka = int(input("Masukkan nilai: "))
    label = getgradelabel(nilai_angka)
    print("Label huruf:", label)
except ValueError:
    print("Input tidak valid. Harus berupa angka bulat.")

print("\n============== NO 2 =============")
huruf = input("Masukkan label huruf: ")
nilai_ipk = konversi_huruf_ke_nilai(huruf)

if nilai_ipk is not None:
    print("Nilai IPK:", nilai_ipk)
else:
    print("Label huruf tidak dikenali.")

print("\n============== NO 3 =============")
try:
    jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))
    daftar_sks = []

    for i in range(jumlah_mk):
        sks = int(input(f"jumlah SKS mata kuliah {i+1}: "))
        daftar_sks.append(sks)

    total = total_sks(daftar_sks)
    print("Total SKS:", total)

except ValueError:
    print("Input tidak valid. Harus berupa angka bulat.")
    
print("\n============== NO 4 =============")


print("Jumlah Data: ", end="")
jumlah = int(input())

daftar_sks = []
daftar_nilai = []

print("--------- input sks ---------")
for i in range(jumlah):
    sks = int(input(f"SKS {i+1}: "))
    daftar_sks.append(sks)

print("\n--------- Input Nilai Mahasiswa ---------")
for i in range(jumlah):
    nilai = int(input(f"Nilai {i+1}: "))
    daftar_nilai.append(nilai)

total = total_nilai_ipk(daftar_sks, daftar_nilai)
print("\nTotal Nilai:", round(total, 2))

print("\n============== NO 5 =============")
print("Jumlah Data: ", end="")
jumlah = int(input())

daftar_sks = []
daftar_nilai = []

print("-------- input sks --------")
for i in range(jumlah):
    sks = int(input(f"SKS {i+1}: "))
    daftar_sks.append(sks)

print("\n-------- input Nilai Mahasiswa --------")
for i in range(jumlah):
    nilai = int(input(f"Nilai {i+1}: "))
    daftar_nilai.append(nilai)

ips = hitung_ips(daftar_sks, daftar_nilai)
print("\nIPS:", ips)