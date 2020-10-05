"""
n-dimensional ODEs:
Backword Euler method + Newton
"""

from matplotlib.pyplot import plot, show                    # Import plotting library
from numpy          import zeros, array, identity  # Import array & zero & identity from numpy
from scipy.linalg   import solve, norm             # Import solve & nirm from scipy.linalg

dt = 0.01                     # Time-step

def main():
    T  = 20                        # Total integration time 
    nt = round(T/dt)               # Number of time-steps
    x  = zeros((2,nt+1))           # Create a matrix: 2 rows and nt+1 columns
    x[:,0]  = array([1,0.2]) 
    
    for it in range(0,nt):
        x[:,it+1] = newton(x[:,it], lambda y: g(y, x[:,it]), dg)
    
    t = array(range(0,nt+1))*dt                  # The discrete times that the solution is evaluated on (i.e., the horizontal axis of the following plot)
    plot(t,x[0,:],'ro-',t,x[1,:],'bx-')      # Plot both solution components, now using arrays
    show()
    
    
def g(x1,x):  # test vector-valued function to solve
    return x+dt*f(x1)-x1

def dg(x1): # Jacobian matrix of g(x)
    return dt*df(x1) - identity(2)

def f(x):
    return array([-4*x[1]*x[0]**2, 2*x[0]**2-0.1*x[1]])

def df(x):  # Jacobian matrix of f(x) 
    return array([[((-8)*x[1]*x[0]),((-4)*(x[0]**2))],[(4*x[0]),(-0.1)]])

# Using Newtons method to get root:
def newton(x,g,dg):
    k = 1
    tol = 1e-10
    
    while norm(g(x))>tol and k<100: 
        v = solve(dg(x),g(x))
        x = x - v
        k = k + 1 

    #print('Newtons: ',k,'\t',x,norm(g(x)))

    return x



main()
