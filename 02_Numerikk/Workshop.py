# Numeric-workshop (notes):
from math import sqrt

def main():
    while True:
        print("[-1] - Random | [0] - exit | [1] - list2set | [2] - Precision")
        choice = int(input("Choose a method: "))

        if choice is 0:
            break
        elif choice is -1:
            test()
        elif choice is 1:
            list2set()
        elif choice is 2:
            preci()



def test():
    x = {}
    print(type(x))

def preci():
    print('\n')
    for i in range(3):
        if i is 0: a = 10**8; b = 1; c = 1
        elif i is 1: a = 1; b = 10**8; c = 1
        elif i is 2: a = 1; b = 1; c = 10**8
        try:
            x1 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
            x2 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
            print(f"Calculation #{i+1}")
            print(f' x1 = {x1} \t x2 = {x2}')
        except ValueError as VE:
            print(f"Unable to run calculation #{i+1}\n {VE}")
        finally:
            print('\n')

def list2set():
    l = [1,1,2,5,3,2,2,6]
    s = set(l)
    c = 0
    print("list:\tset:")
    for i in s:
        print(f'  {l[c]}\t {i}')
        c += 1
    if not c is len(l)-1:
        while c < len(l):
            print(f'  {l[c]}')
            c += 1
main()
