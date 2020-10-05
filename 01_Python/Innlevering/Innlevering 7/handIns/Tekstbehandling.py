#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving7.ipynb">Øving 7</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li ><a href="Aksessering.ipynb">Aksessering av karakter</a></li>
#     <li ><a href="Strenger%20og%20konkatinering.ipynb">Konkatinering</a></li>
#     <li ><a href="Slicing.ipynb">Slicing</a></li>
#     <li class="active"><a href="Tekstbehandling.ipynb">Tekstbehandling</a></li>
#     <li ><a href="Strenghandtering.ipynb">Strenghåndtering</a></li>
#     <li ><a href="Innebygde%20funksjoner.ipynb">Innebygde funksjoner og lister</a></li>
#     <li><a href="Fjesboka.ipynb">Fjesboka</a></li>
#     <li ><a href="Akkorder%20og%20toner.ipynb">Akkorder og toner</a></li>
#     <li ><a href="Ideel%20gasslov.ipynb">Ideel Gasslov</a></li>
#     <li><a href="Sammenhengende%20tallrekke.ipynb">Sammenhengende Tallrekke</a></li>
#     <li ><a href="Sortering.ipynb">Sortering</a></li>
#     <li ><a href="Strengmanipulasjon.ipynb">Strengmanipulasjon</a></li>
#     <li ><a href="Kryptering.ipynb">Kryptering</a></li>
#     <li ><a href="Litt%20sjakk.ipynb">Litt Sjakk</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Tekstbehandling
# 
# **Læringsmål:**
# 
# * Strenger
# * Funksjoner
# * Løkker
# * Kodeforståelse
# 
# **Starting Out with Python:**
# 
# * Kap. 8.3

# ## Generelt om testing, søking og manipulering av strenger

# **Testing av strenger:**
# 
# Python har to nyttige operatoerer `in` og `not in`. Disse kan brukes til å sjekke om en streng er inneholdt i en annen.
# 
# >La streng 1 og streng 2 være tilordnet to forskjellige strenger.
# Det logiske uttrykket:
# ```python
# streng1 in streng2
# ```
# vil returnere True om streng1 er inneholdt i streng2, f.eks vil uttrykket
# ```python
# "Ber" in "Bob Bernt"
# ```
# returnere True, mens uttrykket
# ```python
# "obo" in "Bob Bernt"
# ```
# returnerer False.
# Tilsvarende vil det logiske uttrykket
# ```python
# streng1 not in streng2
# ```
# returnere True om streng1 IKKE er inneholdt i streng2, altså det motsatte av det streng1 in streng2 ville returnert.
# 
# Strenger i Python har flere metoder som kan brukes til å teste en streng for bestemte karaktertrekk. Tabellen under viser enkelte av disse:
# 
# ![img](./../../Resources/Images/Innebygde_strengfunksjoner.png)
# 
# Generelt format for bruk av disse metodene er: streng.metode(argument)
# 
# F.eks. vil `streng.isupper()` returnere *True* om alle bokstavene i streng er blokkbokstaver og lengden til strengen er større eller lik 1.
# 
# Metodene i tabellen over er boolske metoder som vil returnere enten *True* eller *False*.
# 
# **Modifisering av strenger:**
# 
# Strengemodifiserings-metoder (se tabellen nedenfor) er metoder som returnerer en modifisert kopi av strengen metoden kalles på. På denne måten kan man "simulere" at strenger endres, enda de ikke egentlig vil dette (strenger er jo ikke-muterbare).
# 
# ![img](./../../Resources/Images/flere-innebygde-strengfunksjoner.png)
# 
# F.eks. vil 
# >```python
# " Cake is good ".strip()
# ```
# 
# returnere strengen "Cake is good".
# 
# **Søking i strenger og erstatting av karakterer:**
# 
# Det finnes også flere metoder som kan søke og finne substrenger i en streng, om de skulle være til stede. I tillegg er det mulig å bruke metoden `streng.replace(old,new)` til å få en kopi av streng der alle instanser av *old* er erstattet med instanser av *new*.
# 
# **Eksempel på bruk av replace(old,new):**

# In[ ]:


s = "I like cake, and I also like ice cream."
s = s.replace("like","love")        #Argumentene old og new må være strenger. Husk at s.replace(old,new) IKKE endrer på strengen s, men returnerer en modifisert kopi av denne. Det er dermed viktig å tilordne en variabel til den modifiserte strengen om den skal brukes senere.
print(s)


# Nedenfor følger en tabell med oversikt over søke- og erstatnings-metoder:
# ![hei](https://www.ntnu.no/wiki/download/attachments/121671061/image2018-6-19%2014%3A15%3A10.png?version=1&modificationDate=1529410607000&api=v2)

# ## Kort om repetisjons-operatoren og splitting av strenger

# **Repetisjons-operatoren:**
# 
# Som du alt har lært, kan man duplisere en liste vha. repetisjons-operatoren *. Det samme gjelder for strenger. Det generelle formatet er:
# 
# *streng * n*
# 
# Dette vil gi en streng bestående av n repeterte kopier av strengen *streng*.
# 
# **Eksempler på bruk av split: (kjør koden)**

# In[ ]:


#Eks 1
s = "bla"*5
print(s)
  
#Eks 2
for i in range(1,5):
    print('X'*i)


# **Splitting av en streng:**
# 
# Python har en metode kalt *split* som returnerer en liste med ordene i strengen metoden blir kalt på. Dvs. at `s.split()` returnerer en liste bestående av ordene i strengen s.
# 
# *split*-metoden kan ta inn en streng som argument. Om *split*-metoden ikke får inn noe argument vil den bruke mellomrom som skilletegn. Om den derimot får inn et argument, f.eks. '-', vil den splitte på disse, og ikke mellomrom.

# In[ ]:


#Eks 1
s = "Lilac and gooseberries"
liste = s.split()           #Vil bruker standard-skilletegnet som er mellomrom
print(liste)
  
#Eks 2
s = "ISBN 978-0-765-32635-5"
liste = s.split('-')        #Vil bruke '-' som skilletegn
print(liste)
  
#Eks 3
s = "Numuhukumakiaki'aialunamor"
liste = s.split('u')        #Vil bruke 'u' som skilletegn
print(liste)

#Eks 4
s = "98765439876542987698762498721598652976298763"
liste = s.split('987')      #Vil bruke '987' som skilletegn
print(liste)


# ## a)

# Skriv en funksjon som tar inn en streng som argument, og endrer bokstavene i den til blokkbokstaver. I tillegg skal funksjonen fjerne eventuell whitespace på start og slutt av strengen. Den resulterende strengen skal så returneres.
# 
# **Eksempel på kjøring:**
# ```python
# streng = " \n  Far over the Misty Mountains \t "
# output -> FAR OVER THE MISTY MOUNTAINS
# ```
# 
# ***Skriv koden din i kodeblokken under:***

# In[7]:


def allCapsRage(str):
    str = str.upper()
    str = str.strip()
    return str

str = '  \n  Far over the Misty Mountains \t '
print(str)
print(allCapsRage(str))


# ## b)

# Lag en funksjon som tar inn en streng og en karakter som argumenter. Funksjonen skal splitte strengen med hensyn på denne karakteren, og returnere listen man får av denne splittingen.
# 
# >```python
# streng = "Hakuna Matata", karakter = 'a'
# output -> ['H', 'kun', ' M', 't', 't', '']```
# 
# ***Skriv koden din i kodeblokken under***

# In[13]:


def main():
    str = []
    str.append('  \n  Far over the Misty Mountains \t ')
    str.append('Hakuna Matata')
    char = 'a'
    
    # Printer:
    for i in range(0,len(str)):
        print(allCapsRage(str[i]))
        print(splitOnA(str[i],char))
    
    
def allCapsRage(str):
    str = str.upper()
    str = str.strip()
    return str
def splitOnA(str,param):
    str = str.split(param)
    return str
    
    
main()


# ## c)

# Hva vil følgende kodesnutt skrive ut til skjerm?
# >```python
# s1 = "eat"
# s2 = "I want to be like a caterpillar. Eat a lot. Sleep for a while. Wake up beautiful."
# def func(s1, s2):
#     s = "My bed is a magical place where I suddenly remember everything I forgot to do."
#     if s1 in s2.lower():
#         s = "The more you weigh, the harder you are to kidnap. Stay safe. Eat cake."
#     print(s)
#     ```
#     >```
# func(s1,s2)
# ```

# **Svar:** The more you weigh, the harder you are to kidnap. Stay safe. Eat cake.
#    

# ## d)

# Skriv en funksjon som, vha. løkker og repetisjons-operatoren, skriver ut følgende til skjerm:
#     
# >```
# Z
# ZZ
# ZZZ
# ZZZZ
# ZZZZZ
# ZZZZZZ
# ZZZZZZZ
# ZZZZZZZZ
# ZZZZZZZ
# ZZZZZZ
# ZZZZZ
# ZZZZ
# ZZZ
# ZZ
# Z
# ```
# 
# ***Skriv koden din i kodeblokken under:***

# In[7]:


def main():
    print('\t\tNumber of lines will be approximated to fit the pattern~~')
    length = str(input('Numer of sleeplines: '))
    if not length:
        length = "16"
    length = int(length)
    lengthOfSleep = int(round(length,0))+1
    sleep(lengthOfSleep)
    
def sleep(n):
    for i in range(1,int(n/2)):
        print('Z'*i)
    for i in range(int(n/2),0,-1):
        print('Z'*i)

    
main()


# #### Hint

# Bruk to for-løkker (IKKE nøstede løkker), der den første teller opp, f.o.m. 1 t.o.m. 7, og den andre teller ned, f.o.m. 8 t.o.m. 1.  
# Se også "Eksempler med repetisjons-operatoren" under "Kort om repetisjons-operatoren og splitting av strenger".
