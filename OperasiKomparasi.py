# Operasi Komparasi 

# Setiap hasil operasi komparasi adalah

#>,<,>=,<=,==,!=,is,is not

#>,<,>=,<=,==,!= (Bisa bekerja di syntax literal)
# is,is not (membandingkan memory / object)

a = 4
b = 2

print('===============LEBIH BESAR DARI(>)================')
# Lebih Besar Dari
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)


print('===============KURANG DARI (<)================')
# Lebih Besar Dari
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)


print('===============LEBIH DARI Sama Dngan (>=)================')
# Lebih Besar Dari
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

print('===============KURANG DARI SAMA DENGAN(<=)================')
# Lebih Besar Dari
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

print('=============== SAMA DENGAN(=)================')
# Sama Dengan
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

print('=============== TIDAK SAMA DENGAN(!=)================')
# Sama Dengan
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

#'is' sebagai komparasi object identitty

x = 5 #ini adalah assigment membuat object
y = 5
print ('nilai x =',x,',id = ',hex(id(x)))
print ('nilai y =',y,',id = ',hex(id(y)))

hasil = x is y
print ('x is y =',hasil)


x = 5 #ini adalah assigment membuat object
y = 6
print ('nilai x =',x,',id = ',hex(id(x)))
print ('nilai y =',y,',id = ',hex(id(y)))

hasil = x is y
print ('x is y =',hasil)


#'is not' sebagai komparasi object identitty
x = 5 #ini adalah assigment membuat object
y = 5
print ('nilai x =',x,',id = ',hex(id(x)))
print ('nilai y =',y,',id = ',hex(id(y)))

hasil = x is not y
print ('x is  y =',hasil)


x = 5 #ini adalah assigment membuat object
y = 6
print ('nilai x =',x,',id = ',hex(id(x)))
print ('nilai y =',y,',id = ',hex(id(y)))

hasil = x is not y
print ('x is y =',hasil)