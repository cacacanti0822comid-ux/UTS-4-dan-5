import math

def persegi(s):
    kel = 4 * s
    area = s * s
    return kel, area

def persegi_panjang(p, w):
    kel = 2 * (p + w)
    area = p * w
    return kel, area

def segitiga(a, t, x, y, z):
    kel = x + y + z
    area = 0.5 * a * t
    return kel, area

def jajar_genjang(a, t, m):
    kel = 2 * (a + m)
    area = a * t
    return kel, area

def layang_layang(d1, d2, u, v):
    kel = 2 * (u + v)
    area = 0.5 * d1 * d2
    return kel, area

def belah_ketupat(d1, d2, s):
    kel = 4 * s
    area = 0.5 * d1 * d2
    return kel, area

def trapesium(a, b, t, u, v):
    kel = a + b + u + v
    area = 0.5 * (a + b) * t
    return kel, area

def lingkaran(r):
    kel = 2 * math.pi * r
    area = math.pi * r * r
    return kel, area

def heksagon(s):
    kel = 6 * s
    area = (3 * math.sqrt(3) / 2) * s * s
    return kel, area

def pentagon(s):
    kel = 5 * s
    area = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * s * s
    return kel, area