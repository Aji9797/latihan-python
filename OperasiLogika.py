# Operasi Logika atau Boolean

#not, or, and, xor 


#NOT
print('==== NOT ====')
a = True
c = not a

print ('Data a =',a)
print ('Data c =',c)



#OR (Jika salah satu true maka hasilnya true)
print('==== OR ====')
a = False
b = False
c = a or b
print (a,'OR',b,'=',c)
a = False
b = True
c = a or b
print (a,'OR',b,'=',c)
a = True
b = False
c = a or b
print (a,'OR',b,'=',c)
a = True
b = True
c = a or b
print (a,'OR',b,'=',c)

#AND (Jika salah satu False maka hasilnya False)
print('==== AND ====')
a = False
b = False
c = a and b
print (a,'AND',b,'=',c)
a = False
b = True
c = a and b
print (a,'AND',b,'=',c)
a = True
b = False
c = a and b
print (a,'AND',b,'=',c)
a = True
b = True
c = a and b
print (a,'AND',b,'=',c)

#XOR (Jika salah satu True maka hasilnya True dan sisanya false)
print('==== XOR ====')
a = False
b = False
c = a ^ b
print (a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print (a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print (a,'XOR',b,'=',c)
a = True
b = True
c = a ^ b
print (a,'XOR',b,'=',c)


# Mendefinisikan variabel boolean
a = True
b = False

print("=== 1. Operator AND ===")
# Menghasilkan True JIKA KEDUANYA bernilai True
print(f"True and True   : {True and True}")    # True
print(f"True and False  : {a and b}")         # False

print("\n=== 2. Operator OR ===")
# Menghasilkan True JIKA SALAH SATU atau KEDUANYA bernilai True
print(f"True or False   : {True or False}")   # True
print(f"False or False  : {False or False}")  # False

print("\n=== 3. Operator NOT ===")
# Membalikkan nilai boolean (True jadi False, False jadi True)
print(f"not True        : {not True}")        # False
print(f"not b (False)   : {not b}")           # True

print("\n=== 4. Operator XOR (^) ===")
# Di Python, XOR menggunakan simbol caret (^).
# Menghasilkan True HANYA JIKA SALAH SATU bernilai True (tidak boleh keduanya).
print(f"True ^ False    : {True ^ False}")    # True
print(f"True ^ True     : {True ^ True}")     # False (karena keduanya sama)
print(f"False ^ False   : {False ^ False}")   # False


print("===== CONTOH AND ======")

punya_tiket = True
usia_cukup = 16

# Menggunakan AND
if punya_tiket and usia_cukup >= 17:
    print("Silakan masuk ke studio bioskop!")
else:
    print("Akses ditolak.")

#Skenario: Seorang pelanggan berhak mendapatkan diskon jika dia sudah menjadi member atau jika total belanjaannya lebih dari 500.000. (Cukup salah satu syarat saja yang terpenuhi)
print("===== CONTOH OR ======")
punya_kartu_member = False
total_belanja = 400000

# Menggunakan OR
if punya_kartu_member or total_belanja > 500000:
    print("Selamat! Anda berhak mendapatkan diskon 10%.")
else:
    print("Maaf, Anda belum memenuhi syarat diskon.")



#Skenario: Sistem mengizinkan pengguna untuk mengubah profil hanya jika akun mereka tidak sedang diblokir (not diblokir).
print("===== CONTOH NOT ======")

akun_diblokir = True

# Menggunakan NOT (membalikkan nilai)
if not akun_diblokir:
    print("Akses diizinkan: Silakan ubah profil Anda.")
else:
    print("Akses ditolak: Akun Anda sedang diblokir.")


print("===== CONTOH XOR ======")
pakai_dompet_digital = True
pakai_kartu_kredit = True

# Menggunakan XOR (^) -> True jika hanya salah satu yang True
bisa_dapat_promo = pakai_dompet_digital ^ pakai_kartu_kredit

if bisa_dapat_promo:
    print("Promo berhasil digunakan!")
else:
    print("Promo gagal: Anda harus memilih salah satu metode saja (tidak boleh dua-duanya atau kosong).")