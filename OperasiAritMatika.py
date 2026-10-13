''' 
Urutan yang di dahulukan 
    1. ()
    2. eksponen
    3. Perkalian dna teman-teman * / ** % //
    4. Pertambahan dan pengurangan + - 
      '''


#Operasi aritmatika
a = 20
b = 2

#Operasi Tambah +
hasil = a + b
print (a,'+',b,'=',hasil)

#Operasi Kurang -
hasil = a - b
print (a,'-',b,'=',hasil)

#Operasi pemBagian /
hasil = a / b
print (a,'/',b,'=',hasil)


#Operasi perKalian *
hasil = a * b
print (a,'*',b,'=',hasil)


#Operasi eksponen (pangkat) **
hasil = a ** b
print (a,'**',b,'=',hasil)


#Operasi Modulus %
hasil = a % b
print (a,'%',b,'=',hasil)

#Operasi floor division //
hasil = a // b
print (a,'//',b,'=',hasil)


# Prioritas Operasi, Operational precedence

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x

print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = (x + y) * z
print (x,'+',y,'*',z,'=',hasil)
