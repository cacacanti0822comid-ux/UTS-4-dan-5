import math

def kubus(s):
    return s**3, 6 * s**2

def balok(p, l, t):
    return p * l * t, 2 * (p*l + p*t + l*t)

def prisma_segitiga(a, t_alas, tinggi, sisi1, sisi2, sisi3):
    luas_alas = 0.5 * a * t_alas
    keliling_alas = sisi1 + sisi2 + sisi3
    return luas_alas * tinggi, 2 * luas_alas + keliling_alas * tinggi

def limas_segitiga(a, t_alas, tinggi):
    luas_alas = 0.5 * a * t_alas
    return (1/3) * luas_alas * tinggi, None  
    
def tabung(r, t):
    return math.pi * r**2 * t, 2 * math.pi * r * (r + t)

def kerucut(r, t):
    s = math.sqrt(r**2 + t**2)
    return (1/3) * math.pi * r**2 * t, math.pi * r * (r + s)

def bola(r):
    return (4/3) * math.pi * r**3, 4 * math.pi * r**2

def prisma_segiempat(p, l, t):
    return p * l * t, 2 * (p*l + p*t + l*t)

def limas_segiempat(p, l, t):
    luas_alas = p * l
    return (1/3) * luas_alas * t, None

def torus(r, R):
    return 2 * math.pi**2 * R * r**2, 4 * math.pi**2 * R * r

rumus_bangun_ruang = {
    "kubus": kubus,
    "balok": balok,
    "prisma_segitiga": prisma_segitiga,
    "limas_segitiga": limas_segitiga,
    "tabung": tabung,
    "kerucut": kerucut,
    "bola": bola,
    "prisma_segiempat": prisma_segiempat,
    "limas_segiempat": limas_segiempat,
    "torus": torus,
}

def hitung_bangun_ruang(nama, *args):
    
    if nama not in rumus_bangun_ruang:
        raise ValueError("Bangun ruang tidak tersedia")
    return rumus_bangun_ruang[nama](*args)