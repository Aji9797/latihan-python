# Latihan Logika dan Komparasi

# Membuat gabungan Area rentang dari

#++++++3-----------10++++++++++

inputuser = float(input("masukan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10\n:"))

#++++++3-----------------------------------
#memeriksa angka kurang dari 3
isKurangDari = (inputuser < 3)

print("Kurang dari 3 adalah =",isKurangDari)

#----------10++++++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputuser > 10)

print("lebih dari 10 adalah =",isLebihDari)


isCorrect = isKurangDari or isLebihDari
print("Angka yang ada masukan :",isCorrect)

print("\n",50*"=","\n")
#----------3++++++++10---------
#Kasus irisan

inputuser = float(input("masukan angka yang bernilai\nlebih dari 3 \natau \nKurang dari 10\n:"))

#----------3++++++++
#lebih dari 3
isLebihDari = inputuser > 3
print("Lebih dari 3 adalah =",isLebihDari)

#++++++++10---------
#Kurang dari 10
isKurangDari = inputuser < 10

print("Kurang dari 10 adalah =",isKurangDari)


isCorrect = isKurangDari and isLebihDari
print("Angka yang ada masukan :",isCorrect)



#Soal 
#1. ------0++++++++ 5 ----------- 8 ++++++ 11 ---------
#2. ++++++ 0 ------- 5 ++++++++++ 8 ------- 11 ++++++++


#1.

inputuser = float(input("masukan angka yang bernilai\n Lebih dari 0 \natau \nKurang dari 5\n \n Lebih dari 8 \natau \nKurang dari 11\n:"))

Data_1 = inputuser > 0
Data_2 = inputuser < 5
Data_3 = inputuser > 8
Data_4 = inputuser < 11

Data_5 = Data_1 and Data_2 or Data_3 and Data_4

print ("Hasil dari data",Data_5)