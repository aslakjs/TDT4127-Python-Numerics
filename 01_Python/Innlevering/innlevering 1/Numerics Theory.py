#!/usr/bin/env python
# coding: utf-8

# # Theory - Numerics exercise 1

# #### Using floating point numbers in Python (click the arrow to the left to expand)

# Computers represent numbers, in base 2, as bits. They have a finite amount of bits available, and to keep the number representations equal across programming languages and platforms, standards are made for how a computer is to store numbers internally. To represent decimal numbers, Python uses double precision floating point numbers (doubles). Doubles consist of 8 bytes, i.e. 64 bits $b_0,b_1,...,b_{63}$ that each can take the values 0 or 1. They are used to represent a decimal number $a$ on the form
# $$\mathrm{fl}(a) = (-1)^{b_{0}}*2^{e-1023}*1.b_{1}b_{2}b_{3}....b_{52}.$$
# <br>
# Here, the exponent is given as $e = b_{53}b_{54}b_{55}b_{56}b_{57}b_{58}b_{59}b_{60}b_{61}b_{62}b_{63},$ a base 2 integer. Note that $e = 00000000000$ and $e=1111111111$ are interpreted as $0$ and $\infty$ respectively, so e takes values between 1 and 2046. The mantissa $1.b_{1}b_{2}b_{3}....b_{52}$ is a real number in base 2 with values between 1 and 2:
# $$ 1.b_{1}b_{2}b_{3}....b_{52} = 1 + \sum_{j = 1}^{52}b_{j}2^{-j}. $$
# Since this is a finite sum, we have a finite amount of numbers at our disposal. This means we cannot represent all of the infinitely many real numbers *exactly* as doubles. We can, however, guarantee a certain *precision*.
# <br><br>
# An example of a number that can be exactly represented on this format is 1.25. It is represented as 
# <br>
# $$b_{1} \quad b_{53}b_{54}b_{55}b_{56}b_{57}b_{58}b_{59}b_{60}b_{61}b_{62}b_{63} \quad b_{1}b_{2}b_{3}...b_{52}
# \quad$$
# $$= \quad 0 \quad 0 1 1 1 1 1 1 1 1 1 1 \quad 010000000000000000000000000000000000000000000000000.$$
# <br><br>
# An example of a number that cannot be exactly represented on this format is 9.4. It is represented as
# $$b_{1} \quad b_{53}b_{54}b_{55}b_{56}b_{57}b_{58}b_{59}b_{60}b_{61}b_{62}b_{63} \quad b_{1}b_{2}b_{3}...b_{52}
# \quad$$
# $$= \quad 0 \quad 1 0 0 0 0 0 0 0 0 1 0 \quad 0010110011001100110011001100110011001100110011001100.$$
# <br>
# If you check closely, you will find that $fl(9.4) = 9.4 + 2^{-49} - 0.4 * 2^{-48} = 9.4 + (1-0.8) * 2^{-49} = 9.4 + 0.2 * 2^{-49}$, i.e. there is an error of $ 0.2 * 2^{-49}$.
# 
# <br> <br>
# In general, one can show that for a floating point number the relative truncation error and the absolute truncation error are given by, respectively,
# $$\frac{|\mathrm{fl}(a) - a|}{|a|} \leq \epsilon_{mach} \qquad \mathrm{ and } \qquad |\mathrm{fl}(a) - a| \leq |a|\epsilon_{mach}$$
# where the *machine epsilon* $\epsilon_{mach}$,  is the smallest unit of precision in the mantissa. For doubles, machine epsilon is $2^{-52} = 2.22*10^{-16}$ since the last decimal spot in the mantissa is $b_{51}$, corresponding to the value $2^{-51}£. For other floating point standard, other precisions apply. If you are interested, you can read more about this [here](https://en.wikipedia.org/wiki/Floating-point_arithmetic).

# #### a) How many bits of computer memory are used when storing a double?

# 64 bits

# #### b) How are these bits distributed among sign, exponent and significand?

# 1 bit Sign, 11 bits Exponent, 52 bits Significand

# #### c) What are, in absolute value, the largest and smallest numbers representable as doubles?

# min:2^(-1074) -> max:(2-2^(-52))*2^(1073)

# #### d) Convert the below numbers to doubles, fl(a), and comment for each of them whether it is an exact representation or not. 
# You do not need to find more than the first eight bits of the significand. You are allowed to use an online "double converter" if you like.
# - 0.25
# - 4.5
# - 0.1

# Exact: 0.25, 4.5        Not exact: 0.1

# #### e) Find the absolute round-off error of the numbers below when represented as a double.
# 
# - 3.1415
# - 6.022140857*10^23
# - 0.8*10^(-10)

# 1: -3.814697265625E-9, 2: 0.00000499075, 3: -4.76837158203125E-8
