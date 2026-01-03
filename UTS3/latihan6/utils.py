def jumlah_harga(data_harga):
    return sum(data_harga)

def ubah_list(string_list):
    return list(map(int, string_list.split()))

def hitung_pajak(jumlah_total):
    if jumlah_total > 50000:
        return jumlah_total * 0.103  # pajak 10,3%
    return 0