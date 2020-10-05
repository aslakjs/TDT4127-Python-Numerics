#innlevering 1

#Numerical Derivitives
import math as ma

x=3.14
h=1
#x = float(input("Enter x: "))
#h = float(input("Enter step length, h: "))

f1=ma.sin(x)
f2=ma.sin(x+h)
f3=ma.cos(x)

df=(f2-f1)/h
diff=abs(f3-df)

print("The derivitive of sin(x) at x = {0} with step length {1} is {2}".format(float(x), float(h), df))
print("The difference between the exact value of cos(x) in the point {0} and the numerical approximation is {1} when h is {2}".format(float(x), float(diff), float(h)))



#Jeg elsker ITGK!
print("\n"*10)
print("Next task: \n\n")

print("Norge")
print("")
print("\nAreal (kv.km): {0}".format(385180))
print("Folketall (mill.): {0}".format(5.3))

print("\n"*3)

print("Noen barn sto og hang ved lekeplassen.\nDiskusjonstemaet deres var noe uventet.\n")
print('''- Hvorfor heter'e "Python"?''')
print("- Var'e slanger som laget det? - Nei, Guido van Rossum.")
print('- Likte slanger kanskje da? - Nei, digga "Monty Python".')
print("- Hva er det? Et fjell?")
print("- Nei, engelsk komigruppe. Begynte i '69")
print("- Wow! Var'e fremdeles dinosaurer da?")


print("\n"*2)

print("Heihei, jeg vil visst ikke kompilere jeg :")
print('Halla, så "bra" du ser ut i dag')
print("Hei på deg")
print("Er ikke dette gøy?")


#Kalkulasjoner
print("\n"*10)
print("Next task: \n\n")


#1)
print('5:2-4 =', (5/2)-4)

#2)
print('5·12+6-1 =', (5*12)+6-1)

#3)
print('3(5+2) =', 3*(5+2))

#4)
print('4[(5+3):2 +7] =', 4*(((5+3)/2)+7))

#5)
print('(−4)^(-3)+5·(3−7:2) =', pow((-4), ( -3 )) + ( 5  * ( 3 - ( 7/2 ) )))


print("\n"*10)


print(355, "minutt blir", 355 // 60, "timer og", 355 % 60, "minutt.")
print(403, "sekund blir", 403 // 60, "minutt og", 403 % 60, "sekund.")
print(67, "dager blir", 67 // 7, "uker og", 67 % 7, "dager.")
print(100, "timer blir", 100 // 24, "døgn og", 100 % 24, "timer.")


print("\n"*10)



# ??
# importerer fra math-biblioteket
  
print("|-8|, dvs. absoluttverdien til -8, er", abs(-8))
print(2.544, "avrundet til helt tall er", round(2.544))
print("Funksjonen int() derimot bare kutter vekk desimalene:", int(2.544) )
print(2.544, "avrundet til to desimaler er", round(2.544, 2))
print("Kvadratroten til", 10, "er", ma.sqrt(10))
print("En sirkel med radius 7 har omkrets", 2*ma.pi*7)
print("En sirkel med radius 7 har areal", ma.pi*(7**2))



#Peppes Pizza
print("\n"*10)
print("Next task: \n\n")



Pizza = 750
Studentrabatt = 20/100
Tips = 8/100
ant = int(input("Hvor mange deler på middagen? "))

totalt = (Pizza * (1-Studentrabatt) * (1+Tips) )
print('Total pris:', round(totalt, 2), 'kr')
print('Hvor mange deltok på middagen?', ant)
print('Ettersom dere var', ant, 'personer, så må hver person betale', totalt/ant, 'kroner.')













