#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving1.ipynb">Øving 1</a>
#     </div>
#     <ul class="nav navbar-nav">
#         <li><a href="Intro%20til%20jupyter.ipynb">Intro til Jupyter</a></li>
#       <li ><a href="Jeg%20elsker%20ITGK!.ipynb">Jeg elsker ITGK!</a></li>
#     <li ><a href="Kalkulasjoner.ipynb">Kalkulasjoner</a></li>
#     <li><a href="Input%20og%20variable.ipynb">Input og variable</a></li>
#     <li><a href="Tallkonvertering.ipynb">Tallkonvertering</a></li>
#     <li class="active"><a href="Peppes%20Pizza.ipynb">Peppes Pizza</a></li>
#     <li><a href="Geometri.ipynb">Geometri</a></li>
#     <li><a href="Vitenskapelig%20notasjon.ipynb">Vitenskapelig notasjon</a></li>
#     <li><a href="Tetraeder.ipynb">Tetraeder</a></li>
#     <li><a href="Bakekurs.ipynb">Bakekurs</a></li>
#     <li ><a href="James%20Bond%20and%20Operation%20round().ipynb">James Bond and Operation Round</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Peppes Pizza
# 
# **Læringsmål:**
# 
# * Gjøre enkle kalkulasjoner i python
# * Skrive et enkelt program
# 
# **Starting Out with Python:**
# 
# * Kap. 2
# 
# Du har nettopp spist middag på Peppes Pizza med noen venner, og mottar denne kvitteringen:
# 
#   
# ```python
# Pizza: 750kr
# Studentrabatt: 20%
# Tips: 8%
# ```

# ## a)

# Lag et program som lagrer verdiene fra regningen i variabler. Variablene skal altså være `Pizza`, `Studentrabatt` og `Tips`.
# 
# ***Skriv koden i blokken under***

# In[ ]:


Pizza = 750
Studentrabatt = 20/100
Tips = 8/100

totalt = (Pizza * (1-Studentrabatt) * (1+Tips) )
print(round(totalt, 2), 'kr')


# #### Eksempel på lignende tilfelle

# Bob Bernt var på kino i helgen og mottok denne regningen:
# 
# **Regning fra Prinsen kino:**
#   
# ```python
# Kinobillett: 125kr
# Popcorn: 70kr
# Brus: 25kr
# Rabatt = 10%
# ```
# 
# I programmet under er verdiene fra regningen blitt lagret i variablene `Kinobillett`, `Popcorn` og `Brus`.
# 
# **Kode:**
# 
#   
# ```python
# Kinobillett = 125
# Popcorn = 70
# Brus = 25
# Rabatt = 0.10
# ```

# ## b)

# Lag en variabel `totalt` som er lik den totale summen av middagen. Du kan skrive i samme kodeblokk som oppgave a.

# #### Eksempel på lignende tilfelle

# Tar utgangspunkt i regningen fra Prinsen kino som Bob Bernt fikk under Eksempel på lignende tilfelle under oppgave a. For å regne ut den totale summen kan dette gjøres på følgende måte:
# 
#   
# ```python
# Total = (Kinobillett + Brus + Popcorn) * (1-Rabatt)
# ```

# ## c) 

# Gjør slik at brukeren kan skrive inn hvor mange som deltok på middagen, og print ut hvor mye hver person må betale.
# 
# **Eksempel på kjøring:**
# 
#   
# ```python
# Total pris: 648.0
# Hvor mange deltok på middagen? 6
# Ettersom dere var 6 personer, så må hver person betale 108.0 kroner.
# ```
# 
# ***Skriv koden i blokken under***

# In[ ]:


Pizza = 750
Studentrabatt = 20/100
Tips = 8/100
ant = int(input("Hvor mange deler på middagen? "))

totalt = (Pizza * (1-Studentrabatt ) * (1+Tips))
print('Total pris:', round(totalt, 2), 'kr')
print('Hvor mange deltok på middagen?', ant)
print('Ettersom dere var', ant, 'personer, så må hver person betale', totalt/ant, 'kroner.')


# ### Hint

# For at man skal bruke input i beregninger må den gjøres om til en int.
