def input_kasir_dan_barang():
 
    jumlah_kasir = int(input("Berapa jumlah kasir? "))

    hasil_per_kasir = []
    total_barang = 0

    for nomor in range(1, jumlah_kasir + 1):
        barang_input = input(f"Masukkan jumlah barang untuk kasir {nomor} (pisahkan dengan spasi): ")
        daftar_barang = list(map(int, barang_input.strip().split()))

        total_kasir = sum(daftar_barang)
        hasil_per_kasir.append(total_kasir)
        total_barang += total_kasir

    print("\n--- Hasil ---")
    for idx, jumlah in enumerate(hasil_per_kasir, start=1):
        print(f"Kasir {idx} memiliki total {jumlah} barang")
    print(f"Total keseluruhan barang: {total_barang}")