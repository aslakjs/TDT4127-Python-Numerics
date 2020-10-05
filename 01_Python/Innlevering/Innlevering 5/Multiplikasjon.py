#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving5.ipynb">Øving 5</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li><a href="Grunnleggende%20om%20funksjoner.ipynb">Grunnleggende om funksjoner</a></li>
#     <li><a href="Varierte%20funksjoner.ipynb">Varierte funksjoner</a></li>
#     <li><a href="Lokale%20variabler.ipynb">Lokale variabler</a></li>
#     <li><a href="Globale%20variabler.ipynb">Globale variabler</a></li>
#     <li><a href="Euklids%20algoritme.ipynb">Euklids algoritme</a></li>
#     <li><a href="Primtall.ipynb">Primtall</a></li>
#     <li class="active"><a href="Multiplikasjon.ipynb">Multiplikasjon</a></li>
#         <li><a href="Den%20store%20sporreundersokelsen.ipynb">Den store spørreundersøkelsen</a></li>
#     <li><a href="Arbeidsdager.ipynb">Arbeidsdager</a></li>
#     <li><a href="Sekantmetoden.ipynb">Sekantmetoden</a></li>
#     <li><a href="Not%20quite%20Blackjack.ipynb">Not quite Blackjack</a></li>
#         <li><a href="Funksjoner%20og%20Jupyter%20widgets.ipynb">Funksjoner og Jupyter widgets</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Multiplikasjon
# 
# **Læringsmål:**
# - Løkker
# - Funksjoner
# 
# **Starting Out with Python:**
# - Kap. 4.2-4.3

# ## a)

# Skriv en funksjon som tar inn en toleransegrense `tol` og returnerer `prod` og `count`, hvor `prod` er definert som:
# 
# $(1+\frac{1}{1^{2}})(1+\frac{1}{2^{2}})(1+\frac{1}{3^{2}})...$
# 
# og `count` er antall iterasjoner som har blitt kjørt.
# 
# Avslutt iterasjonen når endringen i produktet er mindre enn toleransegrensen `tol`. 
# 
# Skriv ut verdien og hvor mange iterasjoner som trengs. Hvis `tol` er 0.01 skal programmet skrive ut følgende:
# ```
# Produktet ble 3.49 etter 19 iterasjoner.
# ```
# 
# ***Skriv koden i kodeblokken under***

# In[8]:


def thing(tol):
    i = 1
    prod = 1
    while (((prod*(1+(1/i**2))) - prod) >= tol):
        prod *= (1 + (1 / (i**2) ))
        i += 1
    return(prod, i)

tol = 0.01
(prod, count) = thing(tol)
print(f'Produktet ble {round(prod,2)} etter {count} iterasjoner.')


# ## b) (FRIVILLIG) (OG VANSKELIG)

# Denne oppgaven krever at du bruker rekursjon, det vil si at funksjonen "kaller" på seg selv. Dette er en mye brukt programmeringsteknikk som vil bli gjennomgått senere i kurset. 
# 
# Lag en ny funksjon som gjør det samme som a) rekursivt. Avslutt rekursjonen når
# 
# $(1+\frac{1}{k^{2}}) < 1 + tol$
# 
# Skriv også ut rekusjonsdybden
# 
# **Eksempel på kjøring:**
# 
# ```
# Skriv inn tol: 0.01
# Rekursjonsdybden er 10
# Produktet ble: 3.37
# ```
# 
# *Merk: den rekursive funksjonen i b) vil ikke gi samme svar som a) pga. at betingelsene som blir brukt er forskjellige.*
# 
# ***Skriv koden i kodeblokken under***

# In[ ]:




