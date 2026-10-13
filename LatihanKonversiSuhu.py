#latihan Konversi satuan temperature

# program konversi celsius ke satuan lain

print ("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float (input('Masukan suhu dalam celcius :'))
print ('suhu adalah',celcius, "Celcius")


#Reamur
reamur = (4/5) * celcius
print ("suhu dalam reamur adalah", reamur, "Reamur")


#fahrnheit
fahrnheit = ((9/5) * celcius) + 32
print ("suhu dalam fahrenheit adalah", fahrnheit, "Fahrnheit")


#Kelvin
kelvin = celcius + 273
print ("suhu dalam Kelvin adalah", kelvin, "Kelvin")



#Quizz

# Farhenheit to Kelvin

fahrnheit = float (input('Masukan suhu dalam Fahrnheit :'))
kelvin = (fahrnheit - 32) * 5/9 + 273.15

print ('suhu dalam kelvin',kelvin, "Kelvin")

#Kelvin to Farhenheit

kelvin = float (input('Masukan suhu dam Kelvin :'))
fahrnheit = (kelvin - 273.15)*9/5 + 32

print ('suhu dalam Farhenhit',fahrnheit, "Fahrenhit")