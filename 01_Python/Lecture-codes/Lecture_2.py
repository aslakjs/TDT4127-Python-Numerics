#Lecture 2 - Thursday 5th of sept
#Kap-2: Bruk av funksjoner, variabler og input/output
#
#Notater:--------------------------------
#Stepliste:
#   1: Hva skal løses
#   2: Fremgangsmåte
#   3: Løsning



def main():
    a = int(input("Verdi for a = "))
    b = float(input("Verdi for b = "))
    elev = 568
    c = calc(a, b)
    pi = m.pi
    text = "litt text"

    printingEx(c, pi, elev)


def calc(a, b):
    #Basic calculation of a times b
    return a*b


def printingEx(c, pi, elev):
    #Printing solutions:
    #   Printing text with variable:
    #       - "{0}".format(var)
    #       - f"{var}"
    #   Alternate between " and ' to include the other in text
    #   Tripple ''' to include both in text
    print("Svaret ble {0}.".format(c))
    print(f"Svaret ble {c}")
    
    print("Don't do it.")
    print('Dette er en "text".')
    print('''"Don't do it."''')
    print("{0} times {1} = {2}".format(pi, c, pi*c))

    # 'sep = ""' velger hva som skal komme mellom forksjellige elementer
    print("Skolen har følgende antall elever: ",elev,".",sep = "")

    #Formatfunksjon:
    #   {var:.2f} - 2 desimaler og flyttall



from time import sleep
import numpy
import math as m
main()
