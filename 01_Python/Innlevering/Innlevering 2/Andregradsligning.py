#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving2.ipynb">Øving 2</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li><a href="Ulike%20typer%20if-setninger.ipynb">Ulike typer if-setninger</a></li>
#     <li><a href="Sammenligning%20av%20strenger.ipynb">Sammenligning av strenger</a></li>
#     <li><a href="Logiske%20operatorer%20og%20logiske%20uttrykk.ipynb">Logiske operatorer og logiske uttrykk</a></li>
#     <li><a href="Forbrytelse%20og%20straff.ipynb">Forbrytelse og straff</a></li>
#     <li><a href="Aarstider.ipynb">Årstider</a></li>
#     <li><a href="Sjakkbrett.ipynb">Sjakkbrett</a></li>
#     <li><a href="Billettpriser%20og%20rabatter.ipynb">Billettpriser og rabatter</a></li>
#     <li><a href="Skatteetaten.ipynb">Skatteetaten</a></li>
#     <li><a href="Epletigging.ipynb">Datamaskinen som tigget epler</a></li>
#     <li class="active"><a href="Andregradsligning.ipynb">Andregradsligning</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Andregradsligning
# 
# **Læringsmål:**
# - Betingelser
# 
# **Starting Out with Python:**
# - Kap. 3.4

# I denne oppgaven skal du lage et program som tar inn input fra brukeren om tallene i en andregradsligning, og returnerer hvorvidt ligningen har to reelle løsninger, to imaginære løsninger eller én reell dobbeltrot. I tillegg skal programmet returnere løsningene dersom de er reelle.
# 
# Den generelle formen til en andregradsligning er 
# 
# \begin{equation*}
# ax^2 + bx + c = 0
# \end{equation*}
# 
# For å finne ut hvor mange løsninger og hvilket løsningsområde en andregradsligning har, kan man bruke *diskriminanten*
# 
# \begin{equation*}
# d = b^2 - 4ac
# \end{equation*}
# 
# og tabellen:
# 
# Tilfelle|Løsningsområde|Antall røtter
# ---|---|---
# d < 0|Imaginær|2
# d > 0|Reell|2
# d = 0|Reell	1|(dobbeltrot)

# ## a) Finn riktig type løsning

# ***Lag et program som ber om de tre verdiene a, b og c, regner ut d, og forteller brukeren om ligningen har to imaginære løsninger, to reelle løsninger, eller én reell dobbeltrot.***
# 
# Sjekk for alle de tre mulige utfallene:
# 
# - To imaginære løsninger
#   - f.eks.: a = 2, b = 4, c = 9
# - To reelle løsninger
#   - f.eks.: a = 2, b = -5, c = 0
# - Én reell dobbeltrot
#   - f.eks.: a = 2, b = 4, c = 2
#   
# ***Skriv koden under***

# In[21]:


from math import sqrt
from numpy import float128 #using float128 for higher precision, 128 bit compared to dpfloat (64bit)
a = float128(input("Input value 'a': "))
b = float128(input("Input value 'b': "))
c = float128(input("Input value 'c': "))

d = (b**2) - (4*a*c)

# Logic to decide sign in the print-text
bsign = csign = str('-')
if b >= 0:
    bsign = '+'
if c >= 0:
    csign = '+'

# Start of text to minimize the amount of writing throughout code
txt = f'The 2nd degree equation: {a}*x^2 ' + bsign + f' {abs(b)}*x ' + csign + f' {abs(c)} has '


# Logic to determine real, double or img root, then print ans.
if d < 0:
    print(txt + 'two imaginary solutions.')
    
elif d > 0:
    x1 = (-b + sqrt(d)) / (2*a)
    x2 = (-b - sqrt(d)) / (2*a)
    print(txt + 'the solution: x1={0} and x2={1}.'.format(x1, x2))
    
else:
    x1 = (-b + sqrt(d)) / (2*a)
    print(txt + f'one real double root: {x1}')


# ## b) Reelle løsninger

# ***Utvid nå programmet i a) slik at bruker får vite løsningen(e) dersom de(n) er reell(e)***
# 
# Andregradsformelen for å finne løsningen(e) er:
# 
# \begin{equation*}
# x=\frac{-b±\sqrt{d}}{2a}
# \end{equation*}
# 
# **Eksempel på kjøring av kode:**
# 
# ```python
# #Eksempel 1: imaginære løsninger  
# a: 2  
# b: 4  
# c: 9  
# Andregradsligningen 2.00*x^2 + 4.00*x + 9.00 har to imaginære løsninger
# ```
# 
# ```python
# #Eksempel 2: reelle løsninger
# a: 2
# b: -5
# c: 0
# Andregradsligningen 2.00*x^2 -5.00*x + 0.00 har de to reelle løsningene 2.50 og 0.00
# ```
# 
# ```python
# #Eksempel 3: reell dobbeltrot
# a: 2
# b: 4
# c: 2
# Andregradsligningen 2.00*x^2 + 4.00*x + 2.00 har en reell dobbeltrot -1.00
# ```

# ## C) (FRIVILLIG) Loss of significance

# Andregradsformelen kan i enkelte tilfeller gi feil svar. Et slikt tilfelle er når man bruker den på likningen  $x^2+9^{12}x−3=0$ . Om man ønsker å finne røttene til denne likningen, gir standardformelen følgende resultat:
# 
# ```python
# Andregradsligningen 1.00*x^2 + 282429536481.00*x -3.00 har de to reelle løsningene 0.000e+00 og -2.824e+11
# ```
# 
# Her er bare den siste av røttene korrekt. Den første roten er ukorrekt blitt null pga. avrundingsfeil som følge av tap av presisjon i beregningen, korrekt svar ville ha vært:
# 
# ```python
# Andregradsligningen 1.00*x^2 + 282429536481.00*x -3.00 har de to reelle løsningene 1.062e-11 og -2.824e+11
# ```
# Hva kommer denne feilen av? ***Gjør om på programmet slik at det tar hensyn til slike tilfeller.***
# 
# **Eksempel på kjøring**
# ```python
# #a = 0.25, b = 18000, c = 1
# #Gammel kode som gir feil svar:
# Andregradsligningen 0.25*x^2 + 18000.00*x + 1.00 har de to reelle løsningene -0.00 og -72000.00
# #Ny kode som gir korrekt svar:
# Andregradsligningen 0.25*x^2 + 18000.00*x + 1.00 har de to reelle løsningene -5.556e-05 og -7.200e+04
#   
# #a = 10, b = 25000, c = 0.015
# #Gammel kode som gir feil svar:
# Andregradsligningen 10.00*x^2 + 25000.00*x + 0.01 har de to reelle løsningene -0.00 og -2500.00
# #Ny kode som gir korrekt svar:
# Andregradsligningen 10.00*x^2 + 25000.00*x + 0.01 har de to reelle løsningene -6.000e-07 og -2.500e+03
# ```

# #### Hint

# Om du sliter, kan det være nyttig å lese dette:
# 
# - [NumericallyStableSolutionForTheQuadraticEquations](http://www.solipsys.co.uk/cgi-bin/sews.py?NumericallyStableSolutionForTheQuadraticEquation)
# - [Numerically Stable Method for Solving Quadratic Equations](https://people.csail.mit.edu/bkph/articles/Quadratics.pdf)
