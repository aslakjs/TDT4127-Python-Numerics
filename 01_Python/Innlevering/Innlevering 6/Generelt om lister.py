#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving6.ipynb">Øving 6</a>
#     </div>
#     <ul class="nav navbar-nav">
#       <li class="active"><a href="Generelt%20om%20lister.ipynb">Generelt om lister</a></li>
#     <li ><a href="Lett%20og%20blandet.ipynb">Lett og blandet</a></li>
#     <li ><a href="Kodeforstaelse.ipynb">Kodeforståelse</a></li>
#     <li><a href="Vektorer.ipynb">Vektorer</a></li>
#     <li ><a href="Lister%20og%20lokker.ipynb">Lister og løkker</a></li>
#     <li ><a href="Teoridelen%20paa%20eksamen.ipynb">Teoridelen på eksamen</a></li>
#     <li><a href="Gangetabell%20og%20lister.ipynb">Gangetabell og lister</a></li>
#     <li ><a href="Lotto.ipynb">Lotto</a></li>
#     <li ><a href="Tannfeen.ipynb">Tannfeen</a></li>
#         <li><a href="Chattebot.ipynb">Chattebot</a></li>
#     <li ><a href="Matriseaddisjon.ipynb">Matriseaddisjon</a></li>
#     <li ><a href="Intro%20til%20numpy-arrays.ipynb">Intro til numpy-arrays</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Generelt om lister
# 
# **Læringsmål:**
# 
# * Lister
# 
# **Starting Out with Python:**
# 
# * Kap. 7.1-7.3
# 
# I denne oppgaven skal vi bli kjent med hvordan lister fungerer i Python ved å opprette enkle lister, endre på dem, og skrive ut listene til konsollen. 

# In[ ]:





# ### Generelt om lister

# Lister er en mye brukt datastruktur for å tilordne én variabel en rekke med verdier. Lister kan blant annet inneholde tall, strenger eller andre lister.
# 
# For å opprette en tom liste i Python skriver vi []. Vilkårlig lange lister kan lages ved å skrive [a, b, c, ... ], der a, b, og c er elementer i listen. For eksempel:

# In[ ]:


min_liste = [4,'elementer','i','listen']


# Hvert element i en liste har en indeks, som beskriver posisjonen elementet har i listen. Denne brukes når vi skal endre eller finne et element i en liste.
# 
# Lister i Python er nullindeksert, det vil si at det første elementet har indeks 0, det neste elementet har indeks 1, osv. Ved å skrive liste[index] kan vi finne eller endre elementer i en liste. Dvs. at min_liste[0] er 4, min_liste[1] er 'elementer', min_liste[2] er 'i' og min_liste[3] er 'listen'.
# 
# For eksempel: (**Prøv gjerne å endre på koden og se hva som skjer**)

# In[ ]:


min_liste = [4,'elementer','i','listen']
print(min_liste[0])  # koden skriver ut elementet på posisjon 0 i listen: 4
min_liste[1] = 'ting'
print(min_liste[1])  # koden skriver ut elementet på posisjon 1 i listen: ting


# ### a)

# Lag en liste **my_first_list** med alle heltallene fra og med 1 til og med 6.
# 
# Eksempel på kjøring:
# 
# ```python
# print(my_first_list)
# [1, 2, 3, 4, 5, 6]
# ```
# ***Skriv koden din i boksen under.***

# In[2]:


my_very_first_list_OMG = [i for i in range(1,7)]
print(my_very_first_list_OMG)


# ### Lengde av lister

# For å finne lengden på en liste er det nyttig å benytte seg av den innebygde funksjonen, len(). Dersom vi tar len(min_liste) vil dette være lik 4 dersom min_liste er lik som under Generelt om lister. Lengden er altså lik antall elementer i listen. Ettersom en liste er nullindeksert vil indeksen til det siste elementet alltid være lik lengden-1. For eksempel vil det siste elementet i min_liste være på indeks 3 når lengden er 4. En annen måte å få ut det siste elementet i en liste er å tenke at det siste elementet har indeks -1, da vil det nest siste elementet ha indeks -2 osv.

# ### b)

# Skriv ut det siste elementet i listen til skjerm. **Husk at du kan bruke listen fra forrige oppgave uten å definere my_first_list på nytt.**
# 
# (obs: dette kan gjøres på to forskjellige måter)
# 
# Eksempel på kjøring:
# ```python
# 6
# ```
# ***Skriv koden din i boksen under.***

# In[7]:


my_very_first_list_OMG = [i for i in range(1,7)]
x=len(my_very_first_list_OMG) - 1
print(my_very_first_list_OMG[x])


# ### c)

# c) Bytt ut det nest siste elementet (5) med tekststrengen 'pluss'.
# 
# Eksempel på kjøring:
# 
# ```python
# print(my_first_list)
# [1, 2, 3, 4, 'pluss', 6]
# ```
# 
# ***Skriv koden din i boksen under.***

# In[6]:


my_very_first_list_OMG = [i for i in range(1,7)]
x=len(my_very_first_list_OMG) - 1
my_very_first_list_OMG[x-1] = 'pluss'
print(my_very_first_list_OMG)


# ### Slicing av lister

# La oss si at vi har en liste som inneholder 5 elementer, for eksempel

# In[ ]:


bokstaver = ['a', 'b', 'c', 'd', 'e']


# Vi ønsker en ny liste som kun inneholder de første 3 elementene, dvs. 'a', 'b' og 'c', og den listen skal hete bokstaver_abc.

# In[ ]:


bokstaver_abc = bokstaver[:3]
print(bokstaver_abc)


# En generell formel for slicing er:
# 
# nyListe = liste[start:slutt]
# 
# hvor start er indeksen til det første tallet du ønsker å ha med, og slutt er indeksen+1 til det siste tallet du ønsker å ha med. Altså er den formelen skrevet som "fra og med" start og "til, men ikke med" slutt. Dersom man ikke skriver noe på start som i eksempelet over, vil programmet anta at du mener fra starten av listen, og dersom du ikke skriver noe på slutt vil programmet anta at du mener frem til listen er ferdig.

# ### d)

# Lag en ny liste **my_second_list** som skal inneholde de tre siste elementene i **my_first_list**.
# 
# Eksempel på kjøring:
# 
# ```python
# print(my_second_list)
# [4, 'pluss', 6]```
# 
# ***Skriv koden din i boksen under.***

# In[10]:


my_very_first_list_OMG = [i for i in range(1,7)]
x=len(my_very_first_list_OMG) - 1
my_very_first_list_OMG[x-1] = 'pluss'

OMG_a_new_list = [my_very_first_list_OMG[i] for i in range(x-2,x+1)]

print(OMG_a_new_list)


# ### e)

# Skriv ut my_second_list og tekststrengen 'er lik 10' til skjerm.
# 
# Eksempel på kjøring:
# 
# ```python
# [4, 'pluss', 6] er lik 10
# ```
# 
# ***Skriv koden din i boksen under.***

# In[12]:


my_very_first_list_OMG = [i for i in range(1,7)]
x=len(my_very_first_list_OMG) - 1
my_very_first_list_OMG[x-1] = 'pluss'

OMG_a_new_list = [my_very_first_list_OMG[i] for i in range(x-2,x+1)]

print(OMG_a_new_list, 'er lik', 10)


# In[ ]:




