def rupiah(n):
    return "Rp " + "{:,}".format(int(n)).replace(",", ".")