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
#     <li ><a href="Osteviruset.ipynb">Osteviruset</a></li>
#     <li ><a href="Bursdagsdatabasen.ipynb">Bursdagsdatabasen</a></li>
#     <li ><a href="Tallak%20teller%20antall%20tall.ipynb">Tallak teller antall tall</a></li>
#     <li class="active"><a href="Opptaksgrenser.ipynb">Opptaksgrenser</a></li>
#         <li ><a href="Soke%20i%20tekst.ipynb">Søke i tekst</a></li>
#     <li ><a href="Tre%20paa%20rad.ipynb">Tre på rad</a></li>
#     </ul>
#   </div>
# </nav>
# 
# 
# # Opptaksgrenser
# 
# **Læringsmål:**
# 
# * Lese fra filer
# * dictionaries
# 
# **Starting Out with Python:**
# 
# * Kap. 6: Files and Exceptions
# * Kap. 9.1 Dictionaries
# 
# I denne oppgaven skal vi lese inn en fil med opptaksgrensene fra Samordna Opptak.
# 
# Filen er på CSV-format (Comma Separated Values), noe som betyr at hver linje er en liste med felter separert med komma. Tekstfelter er omsluttet av fnutter (").
# 
# * Første felt er studiets navn
# * Andre felt er poenggrensen (enten et tall, eller "Alle" dersom alle kom inn)
# 
# F.eks. linjen: **"NTNU 194459 Antikkens kultur","Alle"** sier at alle som søkte kom inn på Dragvoll-studiet “Antikkens kultur” ved NTNU.
# 
# Hver funksjon i de følgende deloppgavene tar data fra filen **poenggrenser_2011.csv** som input. Derfor er det veldig praktisk å lagre innholdet i en variabel, slik at du slipper å lese den på nytt hver gang.

# ### a)

# Les fra fila `poenggrenser_2011.csv` og lagre innholdet i en variabel.
# 
# ***Skriv koden din i boksen under.***

# In[3]:


grenser = open("poenggrenser_2011.csv")
for i in grenser:
    print(i)


# ### b)

# Skriv en funksjon som finner ut hvor mange studier som tok inn alle søkere. 
# 
# ***Husk at du nå i alle deloppgavene kan bruke variabelen du definerte i a så lenge du har kjørt den kodesnutten først!***
# 
# *Eksempel på kjøring av kode:*
# ```python
# Antall studier hvor alle kom inn: 590
# ```
# ***Skriv koden din i boksen under.***

# In[157]:


def main():
    grenser = getGrenser()
    filledUp = isFull(grenser)
    print(f'Antall studier hvor alle kom inn: {filledUp}')
    
    
def isFull(grenser):
    n = 0
    for i in grenser:
        if "ALLE" in i.upper():
            n += 1
    return n
    
def getGrenser():
    return open("poenggrenser_2011.csv")
main()


# In[ ]:





# In[ ]:





# ### b)

# Skriv en funksjon som finner gjennomsnittlig opptaksgrense for NTNU. Ikke ta med studier som tok inn alle søkere.
# 
# *Eksempel på kjøring av kode:*
# ```python
# Gjennomsnittlig opptaksgrense for NTNU var: 46.29
# ```
# ***Skriv koden din i boksen under.***

# In[193]:


from numpy import array, concatenate

def main():
    school  = "NTNU"
    grenser = getGrenser()
    filled  = isFull(grenser)
    avg     = average(grenser, school)
    
    printf(school,filled,avg)
    
    
def average(grenser, school):
    a = 0
    n = 0
    for i in grenser:
        if not "ALLE" in i.upper() and school in i.upper():
            j = (i.split(','))
            a += float(j[1])
            n += 1       
    return(a/n)
    
    
def isFull(grenser):
    n = 0
    for i in grenser:
        if "ALLE" in i.upper():
            n += 1
    return n
def getGrenser():
    return list(open("poenggrenser_2011.csv"))
def printf(school, filled, avg):
    print(f'Antall studier hvor alle kom inn: \t\t{filled}')
    print(f'Gjennomsnittlig opptaksgrense for {school} var: \t{avg:.2f}')
    
main()


# In[ ]:





# In[ ]:





# #### Hint

# For å sjekke om studiet var på NTNU kan du hente ut de fire første bokstavene i hver linje. Hvis du har en string studie kan du gjøre dette ved å skrive: studie[1:5]

# ### c)

# Skriv en funksjon som finner studiet med laveste opptaksgrense (som IKKE tok inn alle søkere).
# 
# *Eksempel på kjøring av kode:*
# ```python
# Studiet som hadde den laveste opptaksgrensen var: AHO 189343 Industridesign
# ```
# ***Skriv koden din i boksen under.***

# In[251]:


from numpy import array, concatenate

def main():
    school  = "NTNU"
    grenser = getGrenser()
    filled  = isFull(grenser)
    avg     = average(grenser, school)
    low     = lowest(grenser)
    
    printf(school,filled,avg,low)
   

    # NEW function~~
def lowest(grenser):
    mi = 100
    a = 0
    retList = []
    for i in grenser:
        if not "ALLE" in i.upper():
            j = (i.split(','))
            if float(j[1]) < mi:
                mi = float(j[1])
    for i in grenser:
        if str(mi) in i:
            i = i.strip()
            i = i.replace('"','')
            i = i.split(',')
            retList = (i[0]).split()
            retList[1] = int(retList[1])
    return retList

    
    # OLD~~
def average(grenser, school):
    a = 0
    n = 0
    for i in grenser:
        if not "ALLE" in i.upper() and school in i.upper():
            j = (i.split(','))
            a += float(j[1])
            n += 1       
    return(round(a/n,2))
def isFull(grenser):
    n = 0
    for i in grenser:
        if "ALLE" in i.upper():
            n += 1
    return n
def getGrenser():
    return list(open("poenggrenser_2011.csv"))
def printf(school, filled, avg,low):
    print(f'Antall studier hvor alle kom inn: \t\t{filled}')
    print(f'Gjennomsnittlig opptaksgrense for {school} var: \t{avg}')
    print(f'\nStudiet som hadde den laveste opptaksgrensen var:\n\t{low[0]} {low[1]} {low[2]}')
    
main()


# ### d)

# Lag en dictionary som har studiestedet som nøkkel og en liste med dictionaries som verdi. Denne listen med dictionaries skal ha navnet på linjen som nøkkel og opptakspoengene til den tilsvarende linjen som verdi. Dersom en linje har navnet "Fysikk og Matematikk" trenger du kun å ta hensyn til det første ordet, dvs. "Fysikk". 
# 
# **Eksempel på utskrift:**
# 
# ```python
# ATH [{'Kristendom': ' Alle'}, {'Interkulturell': ' Alle'}, {'Musikk': ' Alle'}, {'Teologi': ' Alle'}, {'Kristendom': ' Alle'}, {'Psykologi': ' Alle'}, {'Musikk': ' Alle'}, {'Interkulturell': ' Alle'}, {'Psykologi': ' Alle'}, {'Praktisk': ' Alle'}]
# AHO [{'Arkitekt': '12.3'}, {'Industridesign': '11.7'}]
# BDH [{'Sykepleierutdanning': '45.5'}]
# MF [{'Kristendom/RLE': ' Alle'}, {'Samfunnsfag': ' Alle'}, {'Interkulturell': ' Alle'}, {'Teologi': ' Alle'}, {'Religion': ' Alle'}, {'Ungdom': ' Alle'}, {'Lektor-': ' Alle'}, {'Teologi': ' Alle'}]
# DHS [{'Sykepleierutdanning': '48.3'}, {'Vernepleierutdanning': '41.8'}, {'Sosialt': '49.1'}, {'Sosialt': '42.4'}, {'Ergoterapeututdanning': '32.6'}]
# DMMH [{'Førskolelærerutdanning': '36.3'}, {'Førskolelærer': '39.1'}, {'Førskolelærer': '44'}, {'Førskolelærer': '46.2'}, {'Førskolelærer': ' Alle'}]
# .
# .
# .
# UIT [{'Ingeniør': ' Alle'}, {'Ingeniør': ' Alle'}, {'Ingeniør': ' Alle'}, {'Ingeniør': ' Alle'}, {'Sykepleierutdanning': '43.8'}, {'Lærerutdanning': ' Alle'}, {'Lærerutdanning': ' Alle'}, {'Førskolelærerutdanning': ' Alle'}, ....
# ```
# ***Skriv koden din i boksen under.***

# In[376]:


from numpy import array, concatenate

def main():
    school  = "NTNU"
    grenser = getGrenser()
    filled  = isFull(grenser)
    avg     = average(grenser, school)
    low     = lowest(grenser)
    studies = toDict(grenser)
    printf(school,filled,avg,low,studies)
   

    # NEW function~~"NTNU": dict(),"ATH": dict(),"BDH": dict(),"MF": dict(),"DHS": dict(),"DMMH"
def toDict(grenser):
    studies = dict()
    for i in grenser:
        tempVal = dict()
        j = i.strip()
        j = j.split()
        
        # point grabs søkertall/søkerpoeng
        point = ((j[-1].replace('"','')).split(","))[-1]
        if "ALLE" not in point.upper():
            point = float(point)
        
        j[0] = j[0].replace('"','')
        
        # cource grabs fag-navn
        cource = ((j[2].replace('"','')).split(","))[0]
        
        tempVal = {cource: point}
        
        if j[0] not in studies:
            studies.update({j[0]:[]})
        
        temp = studies.get(j[0])
        temp.append(tempVal)
        studies.update({j[0]:temp})
    return studies

    
    # OLD~~
def lowest(grenser):
    mi = 100
    a = 0
    retList = []
    for i in grenser:
        if not "ALLE" in i.upper():
            j = (i.split(','))
            if float(j[1]) < mi:
                mi = float(j[1])
    for i in grenser:
        if str(mi) in i:
            i = i.strip()
            i = i.replace('"','')
            i = i.split(',')
            retList = (i[0]).split()
            retList[1] = int(retList[1])
    return retList
def average(grenser, school):
    a = 0
    n = 0
    for i in grenser:
        if not "ALLE" in i.upper() and school in i.upper():
            j = (i.split(','))
            a += float(j[1])
            n += 1       
    return(round(a/n,2))
def isFull(grenser):
    n = 0
    for i in grenser:
        if "ALLE" in i.upper():
            n += 1
    return n
def getGrenser():
    return list(open("poenggrenser_2011.csv"))
def printf(school, filled, avg,low,studies):
    print(f'Antall studier hvor alle kom inn: \t\t{filled}')
    print(f'Gjennomsnittlig opptaksgrense for {school} var: \t{avg}')
    print(f'\nStudiet som hadde den laveste opptaksgrensen var:\n\t{low[0]} {low[1]} {low[2]}\n')
    for i in studies:
        print(f'{i}; Antall studieretninger: {len(studies[i])}')
        for j in range(0,len(studies[i])):
            print(f'\t#{j+1}:\t{studies[i][j]}')
        print("\n")
    
main()


# In[ ]:





# In[ ]:





# In[ ]:




