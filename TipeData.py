# a = 10, a adalah Variabel dengan Nilai 10

#tipe data : angka satuan (integer)
data_integer = 1
print ("data : ", data_integer)
print ("data : ", data_integer, ", Bertipe : ", type(data_integer))


#tipe data : angka dengan Koama (float)
#
data_float = 1.5
print ("data : ", data_float)
print ("data : ", data_float, ", Bertipe : ", type(data_float))

#tipe data : Kupulan karakter  (String)
data_string = "aji"
print ("data : ", data_string)
print ("data : ", data_string, ", Bertipe : ", type(data_string))


#tipe data : Biner True / False  (Boolean)
data_boolean = True
print ("data : ", data_boolean)
print ("data : ", data_boolean, ", Bertipe : ", type(data_boolean))


#Tipe Data Khusus

# bilangan kompleks
data_complex = complex (5,6)
print ("data : ", data_complex)
print ("data : ", data_complex, ", Bertipe : ", type(data_complex))


#tipe data dari bahas C

from ctypes import c_double

data_c_double = c_double(10.5)
print ("data : ", data_c_double)
print ("data : ", data_c_double, ", Bertipe : ", type(data_c_double))
