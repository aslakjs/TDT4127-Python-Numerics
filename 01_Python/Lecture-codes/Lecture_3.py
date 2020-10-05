#Lecture 3 - Thursday Sept. 12th
#Kap-2: Bruk av funksjoner, variabler og input/output
#
#Notater:--------------------------------
# if statement, 
# logiske operasjoner (and, or)
# boolsk struktur
# 
# 


def main():
    aartest()     
    # if truefalse == true:
    #     print('A er større enn 0')
    # else:
    #     print('A er mindre enn 0')

    
    


def aartest():
    aar = int(1)
    while not aar == 00:
        aar = int(input('\n\nSkriv inn ett årstall: '))
        if aar % 4 == 0 and aar % 100 == 0 and aar %400 == 0 and aar >= 1582:
            print('\nskuddår')
        elif aar == 00:
            exit
        else:
            print('\nvanlig år')
    



from time import sleep
import numpy
import math as m
from time import sleep
main()
