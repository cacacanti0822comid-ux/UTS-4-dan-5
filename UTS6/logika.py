#1 grading_nilai.py——————————————

def getgradelabel(nilai: int) -> str:
    if 85 <= nilai <= 100:
        return "A"
    elif 80 <= nilai <= 84:
        return "A-"
    elif 75 <= nilai <= 79:
        return "B+"
    elif 70 <= nilai <= 74:
        return "B"
    elif 65 <= nilai <= 69:
        return "B-"
    elif 60 <= nilai <= 64:
        return "C+"
    elif 55 <= nilai <= 59:
        return "C"
    elif 45 <= nilai <= 54:
        return "D"
    elif nilai < 45:
        return "E"
    else:
        return "Nilai tidak valid"
        
#2.logika_huruf.py——————————————————
def konversi_huruf_ke_nilai(huruf: str) -> float:
    huruf = huruf.lower()
    if huruf == "a":
        return 4
    elif huruf == "a-":
        return 3.75
    elif huruf == "b+":
        return 3.5
    elif huruf == "b":
        return 3
    elif huruf == "b-":
        return 2.75
    elif huruf == "c+":
        return 2.5
    elif huruf == "c":
        return 2
    elif huruf == "d":
        return 1
    elif huruf == "e":
        return 0
        
#3.logika_huruf.py——————————————————
def total_sks(daftar_sks):
    total = 0
    for sks in daftar_sks:
        total += sks
    return total

#4.logika_huruf.py——————————————————
#def total_nilai(daftar_nilai_sks):
  #  total = 0
   # for nilai in daftar_nilai_sks:
   #     total += nilai
   # return total
def konversi_nilai_ke_ipk(nilai: int) -> float:
    if 85 <= nilai <= 100:
        return 4
    elif 80 <= nilai <= 84:
        return 3.75
    elif 75 <= nilai <= 79:
        return 3.5
    elif 70 <= nilai <= 74:
        return 3
    elif 65 <= nilai <= 69:
        return 2.75
    elif 60 <= nilai <= 64:
        return 2.5
    elif 55 <= nilai <= 59:
        return 2
    elif 45 <= nilai <= 54:
        return 1
    elif nilai < 45:
        return 0

def total_nilai_ipk(daftar_sks, daftar_nilai):
    total = 0
    for sks, nilai in zip(daftar_sks, daftar_nilai):
        ipk = konversi_nilai_ke_ipk(nilai)
        total += ipk * sks
    return total
    
 #5.logika_huruf.py—————————————————— 
def hitung_ips(daftar_sks, daftar_nilai):
    total_sks = sum(daftar_sks)
    total_nilai = 0
    for sks, nilai in zip(daftar_sks, daftar_nilai):
        ipk = konversi_nilai_ke_ipk(nilai)
        total_nilai += ipk * sks
    if total_sks == 0:
        return 0
    return round(total_nilai / total_sks, 2)  
