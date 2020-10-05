# Bisection method & Newtons method
from math import cos, sin, pi, exp
from numpy import float128

def main():
    #Converges at x0 = 4 ish
    x0 = bisection()
    x = float128(x0)
    y = float128(0)              #y = x_(k+1)
    tol = float128(10**(-10))
    
    k = 1
    while (( abs(f(x)) > tol ) or ( abs(x-y) > tol )) and (k <= 100):
        y = x - ( f(x) / ( df(x) ))
        print('Iteration #{0}: '.format(k), round(y,10))
        x = y
        k += 1
   
    print(f"\nThe value of the derivative at x = {round(x,10)} is f'({round(x,10)}) =", round(df(x),10))
    
    

def f(x):
    return ( x*exp(-sin((1/2)*x)**2)-3/2 )
def df(x):
    return ( exp(-sin((1/2)*x)**2)-x*sin((1/2)*x)*cos((1/2)*x)*exp(-sin((1/2)*x)**2) )


def bisection():
    tol = float128(2)
    xlow = float(input('Lower limit of interval: '))
    xhigh = float(input('Upper limit of interval: '))
    c = xhigh
    i = 1
    while ( abs(f(c)) > tol) and (i <= 100):
        if ( abs(xhigh) > abs(xlow) ): 
            xhigh = (xlow+xhigh)/2
            c = xhigh
            
        else:
            xlow = (xlow+xhigh)/2
            c = xlow
            
        print(xhigh)
        i += 1
    
    return xhigh


main()
