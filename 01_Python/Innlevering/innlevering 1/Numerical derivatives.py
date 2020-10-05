#!/usr/bin/env python
# coding: utf-8

# # Numerical Differentiation
# ###### Learning goals:
# - Functions
# 
# ##### Starting out with python:
# - Ch. 5.5

# ###  Difference approximations (click arrow to the right to expand)

# Sometimes, one cannot find the derivative of a function in the usual manner. This can happen if the function is very hard to differentiate, if you don't know exactly how the function is defined (which can be the case with [black box systems](https://en.wikipedia.org/wiki/Black_box), or if you have little time and don't want to bother differentiating the function.
# 
#  
# 
# In this case, you can approximate the derivative by using difference approximations. The easiest one of these is to choose a small h and using this, approximate the derivative by the value $$f'(x) \approx \frac{f(x+h)-f(x)}{h}.$$
# 
# This approximation is better, the smaller $h$ is. We can see this as following: If we assume that $f$ is twice differentiable, Taylor's theorem states that $$f(x + h) = f(x) + hf'(x) + \frac{h^2}{2}f''(z)$$
# 
# where $z$ is between $x$ and $x+h$. If we rearrange the terms, we find that $$f'(x) = \frac{f(x+h)-f(x)}{h} + \frac{h}{2}f''(z).$$
# 
# Thus, only a term multiplied by $h$ separates the actual derivative from the approximation. This means that the smaller $h$ is, the closer to the true value of the derivative we get.
# 
# 

# ## Programming task

#  **a)** 
#  - Initiate the variables h = 0.001 and x = 3.14. 
#  - Make a variable f1 with the value sin(x). You should use the built-in function sin() from the "math" Python library.
#  - Make another variable f2 with the value sin(x+h)

# In[1]:


# Write your code here
import math as ma

h=0.001
x=3.14

f1=ma.sin(x)
f2=ma.sin(x+h)


# **b)** Expand your program to differentiate sin(x) numerically, by using $$ f'(x) \approx \frac{f2-f1}{h}. $$
# 
# **Example run**: 
# 
# ```python
# The derivative of sin(x) at x = 3.14 , h = 0.001 has the value -0.9999993613873743
# ```

# In[2]:


# Write your code here
import math as ma

h=0.001
x=3.14

f1=ma.sin(x)
f2=ma.sin(x+h)

df=(f2-f1)/h


# **c)** Expand your program such that $x$ and $h$ are given by the user. $x$ and $h$ are *floats*, so you will need to use float(input(...)) here. Calculate the derivative and print the answer to the screen.
# 
# **Example run:**
# ```python
# Enter x: 3.14
# Enter step length, h: 1
#     
# '''
# Example output:
# The derivative of sin(x) at x = 3.14 with step length 1.0 is -0.8422020564666818
# '''
# ```
# 
# Note that the exact value of the derivative of sin(x) is cos(x). cos(3.14) is approximately equal to -1, but in the above example, the value was approximated to -0.8422. This means that the step length h was probably a bit too large, see the above discussion of step lengths versus correct values.

# In[ ]:


# Write your code here

import math as ma
x=float(input('Enter x: ')
h=float(input('Enter step length, h:'))

f1=ma.sin(x)
f2=ma.sin(x+h)

df=(f2-f1)/h


# **d)** 
# - Introduce the variable $f3$ with the value $cos(x)$ in the point x. 
# - Expand your program to print the difference between $cos(x)$ and the numerical approximation to $f'(x)$. 
# - Try with different step lengths h and see how the approximation improves/degrades with the different choices.
#  **Example run:**
#  
# ```python
# Enter x: 3.14
# Enter step length, h: 1
# 
# '''
# Example output:    
# The derivative of sin(x) at x = 3.14 with step length 1.0 is -0.8422020564666818
# The difference between the exact value of cos(x) in the point 3.14 and the numerical approximation is 0.15779667526085772 when h is 1.0
# '''
# 
# Enter x: 3.14
# Enter step length, h: 0.0001
# 
# '''
# Example output: 
# The derivative of sin(x) at x = 3.14 with step length 0.0001 is -0.9999988096956306
# The difference between the exact value of cos(x) in the point 3.14 and the numerical approximation is 7.796809109450464e-08 when h is 0.0001
# '''
# ```

# In[4]:


# Write your code here

import math as ma

x=float(input('Enter x: '))
h=float(input('Enter step length, h:'))

f1=ma.sin(x)
f2=ma.sin(x+h)
f3=ma.cos(x)

df=(f2-f1)/h
diff=abs(f3-df)

print("The derivitive of sin(x) at x = {0} with step length {1} is {2}".format(float(x), float(h), df))
print("The difference between the exact value of cos(x) in the point {0} and the numerical approximation is {1} when h is {2}".format(float(x), float(diff), float(h)))

