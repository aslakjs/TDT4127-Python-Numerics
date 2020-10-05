#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving3.ipynb">Øving 3</a>
#     </div>
#     <ul class="nav navbar-nav">
#       <li ><a href="Intro%20til%20lokker.ipynb">Intro til løkker</a></li>
#     <li ><a href="Mer%20om%20lokker.ipynb">Mer om løkker</a></li>
#     <li><a href="Nostede%20lokker.ipynb">Intro til nøstede løkker</a></li>
#     <li ><a href="Kodeforstaelse.ipynb">Kodeforståelse</a></li>
#     <li class="active"><a href="Gjett%20tallet.ipynb">Gjett tallet</a></li>
#         <li ><a href="Tekstbasert%20spill%202.ipynb">Tekstbasert spill 2</a></li>
#     <li ><a href="Geometrisk%20rekke.ipynb">Geometrisk rekke</a></li>
#     <li ><a href="Fibonacci.ipynb">Fibonacci</a></li>
#     <li><a href="Alternerende%20sum.ipynb">Alternerende sum</a></li>
#     <li ><a href="Hangman.ipynb">Hangman</a></li>
#     <li ><a href="Doble%20lokker.ipynb">Doble løkker</a></li>
#     </ul>
#   </div>
# </nav>
# 
# 
# # Gjettelek
# 
# **Læringsmål:**
# 
# * Løkker
# * Betingelser
# * Innebygde funksjoner
# 
# **Starting Out with Python:**
# 
# * Kap. 4.2-4.3
# 
# I denne oppgaven skal du lage et program som genererer et tilfeldig heltall i et gitt intervall, og deretter lar brukeren gjette på hvilket tall dette er. Dette bør gjøres ved bruk av løkker.
# 
# I denne oppgaven må du benytte deg av biblioteket random. Derfor skal koden din starte med ***import random***.
# 
# Eksempel på bruk av random.randint()
# 
# ```python
# tilfeldigTall = random.randint(1,50)    #gir deg et tilfeldig tall fra og med 1, til og med 50
# tall = random.randint(a,b)              #gir deg et tilfeldig tall mellom a og b. (Fra og med a, til og med b)
# ```
# 
# 

# **a)** Be brukeren om å velge en nedre og en øvre grense for tall han eller hun skal gjette på. Lagre disse to opplysningene i to variabler.
# 
# ***Skriv koden din her:***

# In[5]:


import random as ra
llimit = int(input("Enter lower limit: "))
ulimit = int(input("Enter upper limit: "))

rando = ra.randint(llimit, ulimit)
guess = int()
while (guess != rando):
    guess = int(input("Guess a number: "))
    if (guess > rando):
        print("Your guess is a bit high, try again")
    elif (guess < rando):
        print("Your guess is a bit low, try again")
    else:
        print("Correct! The answer was {0}".format(rando))


# **b)** Lag en variabel TilfeldigTall som genererer et tilfeldig tall i intervallet mellom den øvre og den nedre grensen som brukeren har satt. Fortsett å skriv i samme felt som i oppgave a.

# **c)** Skriv en while-løkke som kjører så lenge brukeren ikke har gjettet riktig svar. Brukeren skal få tilbakemelding for hvert gjett om han eller hun gjettet for lavt, for høyt eller riktig. Fortsett å skriv i samme felt som i oppgave a og b.
# 
# Eksempel på kjøring:
# ```python
# Gi en nedre grense for det tilfeldige tallet: 1
# Gi en øvre grense for det tilfeldige tallet: 100
# Make a guess 50
# The correct number is lower
# Make a guess 25
# The correct Number is higher
# Make a guess 37
# The correct number is lower
# Make a guess 32
# You guessed correct!```
