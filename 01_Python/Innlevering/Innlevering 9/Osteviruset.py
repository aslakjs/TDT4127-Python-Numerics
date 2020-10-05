#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving9.ipynb">Øving 9</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li ><a href="Generelt%20om%20dictionary.ipynb">Generelt om dictionary</a></li>
#     <li ><a href="Innebygde%20funksjoner%20i%20dictionaries.ipynb">Innebygde funksjoner</a></li>
#     <li ><a href="Generelt%20om%20sets.ipynb">Generelt om sets</a></li>
#     <li ><a href="Generelt%20om%20filbehandling.ipynb">Generelt om filbehandling</a></li>
#     <li class="active"><a href="Osteviruset.ipynb">Osteviruset</a></li>
#     <li ><a href="Bursdagsdatabasen.ipynb">Bursdagsdatabasen</a></li>
#     <li ><a href="Tallak%20teller%20antall%20tall.ipynb">Tallak teller antall tall</a></li>
#     <li ><a href="Opptaksgrenser.ipynb">Opptaksgrenser</a></li>
#         <li ><a href="Soke%20i%20tekst.ipynb">Søke i tekst</a></li>
#     <li ><a href="Tre%20paa%20rad.ipynb">Tre på rad</a></li>
#     </ul>
#   </div>
# </nav>
# 
# 
# # Osteviruset
# 
# **Læringsmål:**
# - Dictionary
# 
# **Starting Out with Python:**
# - Kap. 9.1 Dictionaries
# 
# Ostelageret til Tine benytter et smart system som mapper oster med lagerhylleplass. Ostene er indeksert på navn, og hver type ost er mappet til en tuple med hylleplasser hvor nøyaktig én ost av denne typen befinner seg. Kodesnutt viser en liten bit av Tine sin ostedatabase i form av en dictionary. 
# 
# Indeksering av dictionaries er ganske likt indeksering av lister. Den største forskjellen er at indekser (nøkler) kan i tillegg til tall, også være andre datatyper. I denne oppgaven er nøklene strenger. 
# 
# Merk: I denne oppgaven trenger du ikke lage noen ekstra funksjoner. Bruk gjerne innebygde funksjoner/metoder som dict.items og str.split for å løse oppgaven.
# 
# ***Kjør kodeblokken under slik at du kan bruke dictionarien i oppgavene lenger ned***

# In[ ]:


cheeses = {
  'cheddar': ('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
  'mozarella': ('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
  'gombost': ('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
  'geitost': ('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
  'port salut': ('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
  'camembert': ('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
  'ridder': ('GOMBOS-4', 'B16-3'),
}


# ## a)

# Finn og skriv ut alle hylleplasser til osten “port salut”. Dvs. skriv ut verdien til denne nøkkelen.
# 
# ***Skriv koden i kodeblokken under***

# In[3]:


cheeses = {
  'cheddar': ('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
  'mozarella': ('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
  'gombost': ('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
  'geitost': ('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
  'port salut': ('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
  'camembert': ('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
  'ridder': ('GOMBOS-4', 'B16-3'),
}

print(cheeses['port salut'])


# Riktig utskrift skal være:
# ```
# ('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4')
# ```

# ## b)

# Dessverre så har hyllene fra B13 til B15, samt hyllene A234, A235 og C31 blitt infisert av et ostespisende virus! Finn alle typer oster som potensielt er smittet av viruset og legg disse til i en liste `infected_cheeses`.
# 
# *Utskrift av infected_cheeses bør nå se slik ut:*
# ```
# Potentially infected cheeses:  ['mozarella', 'camembert', 'cheddar', 'port salut']
# ```
# 
# ***Skriv koden din i kodeblokken under og sjekk at den er riktig***

# In[28]:


def main():
    cheeses = getDict()
    getInfection(cheeses)

    
def getInfection(cheeses):
    infected = set([])
    for i in cheeses:
        for j in cheeses[i]:
            if 'B13' in j.upper() or 'B14' in j.upper() or 'B15' in j.upper() or 'A234' in j.upper() or 'A235' in j.upper() or 'C31' in j.upper():
                infected.add(i)
    infected = list(infected)
    print(f'Potentially harmfull cheeses: {infected}')

    
def getDict():
    cheeses = {
    'cheddar': ('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
    'mozarella': ('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
    'gombost': ('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
    'geitost': ('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
    'port salut': ('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
    'camembert': ('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
    'ridder': ('GOMBOS-4', 'B16-3'),
    }
    return cheeses
main()


# ## c)

# Tross osteviruset, ønsker Tine fortsatt å selge ost til det sultne norske folk. Finn alle typer ost der ingen individ er smittet av viruset, og skriv ut resultatet på formen <hylleplass\> <ostetype\>.
# 
# ***Skriv koden din i kodeblokken under***

# In[3]:


def main():
    cheeses = getDict()
    infection = getInfection(cheeses)
    getSurvivors(cheeses,infection)

    
def getSurvivors(cheeses,infection):
    print("Safe-to-eat cheeses:")
    for i in cheeses:
        if i in infection:
            pass
        else:
            for j in cheeses[i]:
                print(f'\t{j:<{11}}{i}')
    
    
def getInfection(cheeses):
    infected = set([])
    for i in cheeses:
        for j in cheeses[i]:
            if 'B13' in j.upper() or 'B14' in j.upper() or 'B15' in j.upper() or 'A234' in j.upper() or 'A235' in j.upper() or 'C31' in j.upper():
                infected.add(i)
    infected = list(infected)
    print(f'Potentially harmfull cheeses: \n\t{infected}\n')
    return infected

def getDict():
    cheeses = {
    'cheddar': ('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
    'mozarella': ('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
    'gombost': ('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
    'geitost': ('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
    'port salut': ('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
    'camembert': ('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
    'ridder': ('GOMBOS-4', 'B16-3'),
    }
    return cheeses
main()


# Riktig utskrift skal være:
# >```
# ZLAFS55-4  gombost  
# ZLAFS55-9  gombost  
# GOMBOS-7   gombost  
# A236-4     gombost  
# SPAZ-1     geitost  
# SPAZ-3     geitost  
# EMACS45-0  geitost  
# GOMBOS-4   ridder   
# B16-3      ridder
# ```
