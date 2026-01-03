def kalkulasi_rerata(daftar_nilai):
    return sum(daftar_nilai) / len(daftar_nilai) if daftar_nilai else 0.0

def jalankan_program_mahasiswa():
    total_siswa = int(input("Masukkan Jumlah Mahasiswa: "))

    kumpulan_nilai = []
    for nomor_siswa in range(1, total_siswa + 1):
        input_nilai = input(f"Masukkan Nilai Mahasiswa {nomor_siswa}: ")
        nilai_siswa = list(map(float, input_nilai.strip().split()))
        kumpulan_nilai.append(nilai_siswa)

    for nomor_siswa, nilai_siswa in enumerate(kumpulan_nilai, start=1):
        hasil_rerata = kalkulasi_rerata(nilai_siswa)
        print(f"Rata - Rata Nilai Mahasiswa {nomor_siswa}: {hasil_rerata:.2f}")