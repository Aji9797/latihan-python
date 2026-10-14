#Menghitung lingkaran

import math

def hitung_lingkaran(jari_jari):
    #Menghitung luas lingkaran: pi * r^2
    luas = math.pi * (jari_jari ** 2)

    #menghitung keliling lingkaran: 2* pi * r
    keliling = 2 * math.pi * jari_jari

    return luas, keliling

#meminta input pengguna 

try:
    r = float(input("masukan jari-jari lingkaran:"))

    if r < 0:
        print("jari - jari tidak boleh negatif")
    else:
        luas, keliling = hitung_lingkaran(r)

        print("\n=== Hasil Perhitungan ===")
        print(f"jari-jari :{r} cm")
        print(f"Luas :{luas:.2f}cm²")
        print(f"Keliling :{keliling:.2f}cm")

except ValueError:
    print("Mohon Msukan Angka Yang Valid!")

