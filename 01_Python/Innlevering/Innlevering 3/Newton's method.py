#!/usr/bin/env python
# coding: utf-8

# [Back to Assignment 3](_Oving3.ipynb)
# 
# # Newton's method
# In this exercise you will use Newton's method for finding roots of the scalar function $f(x)$ to within a certain level of prescision (i.e., some small number $\texttt{tol}$). Recall that with Newton's method, you make a guess for the root $x_0$, and then you draw a tangent line of $f(x)$ line at $x=x_0$. You then use the root of the tangent line as an $\it{improved}$ guess of the root, which we will call $x_1$. We then draw another tangent line, now at the point $x_1$ and keep going $n$ times until your guess $x_{n}$ satifies some sort of stopping criteria. 
# 
# Newton's method reads $$x_{k+1}=x_{k}-\frac{f(x_{k})}{f'(x_{k})},$$ which is the solution to the root of the tangent line of $f(x)$ at $x=x_k$. Note that this is best implemented using a while loop. 
# 
# **Stopping criteria**: Your stopping criteria should be something like $\texttt{abs}(f(x_n))<\texttt{tol}$ and/or $\texttt{abs}(x_n-x_{n+1})<\texttt{tol}$. In addition, it is sometimes wise to add another stopping criteria in case the algorithm $\it does~not$ converge, for example 
# 
#     k=1
#     while <<stopping_criteria>> and k<100:
#         <<Newton iteration>>
#         k = k+1
#         
# this will stop the loop if it hasn't converged in 100 iterations.
# 
# 

# ## a) 

# Use Newton's method to calculate the roots of the test function $f(x)=\cos(x)$, which has known roots at $x = \frac{n \pi}{2}$, for some integer $m$. 
# 
# Use a tolerance of $\texttt{tol} = 10^{-10}$, and an initial guess of $x_0 = 0.5$.
# 
# Your algorithm should converge to the root $x = \frac{\pi}{2}$. 

# In[25]:


# Newtons method

from math import cos, sin, pi
from numpy import float128

def main():
    #x = float128(input('Enter your initial guess: '))
    x = float128(0.5)
    y = float128(0)              #y = x_(k+1)
    tol = float128(10**(-10))
    
    k = 1
    while (( abs(f(x)) > tol ) or ( abs(x-y) > tol )) and (k <= 100):
        y = x - ( f(x) / ( df(x) ))
        print(f'Iteration #{k}: ', y)
        x = y
        k += 1
    
    print('Goal: (pi)/2 =', pi/2)


def f(x):
    return cos(x)

def df(x):
    return (-sin(x))

main()


# ### i) ###
# For the stopping criteria $\texttt{abs}(f(x_n))<\texttt{tol}$, how many iterations does it take for Newton's method to converge to the root? 
# 
# 

# **Answer:** 5 iterations

# ### ii) ### 
# What happens when you use the initial guess of $x_0 = 0$? Can you explain your observation? (Note: if you have written your code correctly, something $\it should$ go wrong.)

# **Answer:** at x0 = 0, the derivitive of cos(0) will be sin(0) = 0... and deviding by 0 does not work

# ### iii)

# What happens when you use a tolerance of $\texttt{tol} = 10^{-18}$ and $x_0=0.5$? Does the algorithm converge? Can you explain your observation?

# **Answer:** As the tolerance is so small, the algorithm will not converge, as the 100 iteration won't be enough to get close enough to the correct answer, also, pi/2 has a max precition of 10^(-16), thus the algorithim would never reach the set tolerance 

# ## b)

# Now we will try and find a solution to the following function $$x{{\rm e}^{- \left( \sin \left( x/2 \right)  \right) ^{2}}}=3/2. $$ To do this we will look for a root of the function $$ f(x) = x{{\rm e}^{- \left( \sin \left( x/2 \right)  \right) ^{2}}}-3/2.$$
# which has the derivative $$f'(x) = {{\rm e}^{- \left( \sin \left( x/2 \right)  \right) ^{2}}}-x\sin
#  \left( x/2 \right) \cos \left( x/2 \right) {{\rm e}^{- \left( \sin
#  \left( x/2 \right)  \right) ^{2}}}.
# $$ The values of $f(x)$ and $f'(x)$ for $x = 2$ have been written in Python for you below so you don't make a mistake copying the formula into you code. 

# In[39]:


import math 
x = 2
f = x*math.exp(-math.sin((1/2)*x)**2)-3/2
dfdx = math.exp(-math.sin((1/2)*x)**2)-x*math.sin((1/2)*x)*math.cos((1/2)*x)*math.exp(-math.sin((1/2)*x)**2)
print("The value of the derivative at x = 2 is f'(2) =", dfdx)


# Notice that the value for the derivative at $x=2$ is very close to zero and is therefore not a good starting point. 

# ### i) ### 
#  There is a root in the interval $[0,10]$. What is the value of this root? Express your answer to 10 decimal places.  
# 
# **Note:** As suggested above, the Newton method might not converge for certain initial values, therefore you need to test a few initial starting points until the algorithm converges. 
# 

# In[23]:


# Newtons method
from math import cos, sin, pi, exp
from numpy import float128

def main():
    #Converges at x0 = 4 ish
    x = float128(input('Enter your initial guess: '))
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

main()


# #### **Hint:**

# 
# The below code can be used to print values to many decimal places. To get 10 decimal places of accuracy, you should keep iterating your code until the first 10 decimal places of ${x_n}$ don't change between iterations

# In[36]:


n = 1
x = 1/7
f = x*math.exp(-math.sin((1/2)*x)**2)-3/2

print("n = %-2d: x_n = %.10f, f(x_n) = %.5e" % (n,x,f)) 
# this prints the integer n, the float x to 10 decimal places
# ... and the float f to 5 decimal places (in exponential format). This 
# ... is best placed inside your loop to see what is happening at each iteration 


# ### ii) (Optional bonus question for an extra reward*!) ###

# As you may have noticed, Newton's method sometimes doesn't converge unless we are close enough to the solution. One very common method to cirmumvent this issue is to do a few bisection method iterations first, and when you are "close enough" to the solution you can bring it home with Newton iterations. 
# 
# Implement a root finding algorithm that:
# 
#    (1) uses the bisection method until you are within $|f(c)|<\texttt{tol1}$, then
#     
#    (2) uses Newton's method until  $|f(x_n)|<\texttt{tol2}$, 
#     
# where you can choose the values of $\texttt{tol1}$ and $\texttt{tol2}$ as long as $\texttt{tol1}>\texttt{tol2}$.

#  \* The reward is the satisfaction of completing the hardest part of the assignment (+ read the assignment approval description for assignment 3)

# In[52]:


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
        print("Newton's iteration #{0}:\t{1}".format(k, round(y,10)))
        x = y
        k += 1
   
    print(f"\nThe value of the derivative at x = {round(x,10)} is f'({round(x,10)}) =", round(df(x),10))
    

    

def f(x):
    return ( x*exp(-sin((1/2)*x)**2)-3/2 )

def df(x):
    return ( exp(-sin((1/2)*x)**2)-x*sin((1/2)*x)*cos((1/2)*x)*exp(-sin((1/2)*x)**2) )

def bisection():
    tol = float128(1)
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
            
        print("Bisection iteration #{0}:\t{1}".format(i,c))
        i += 1
    
    return c


main()


# In[ ]:





# In[ ]:




