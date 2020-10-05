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
#     <li ><a href="Tekstbehandling.ipynb">Tekstbehandling</a></li>
#     <li ><a href="Strenghandtering.ipynb">Strenghåndtering</a></li>
#     <li ><a href="Innebygde%20funksjoner.ipynb">Innebygde funksjoner og lister</a></li>
#     <li class="active"><a href="Fjesboka.ipynb">Fjesboka</a></li>
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
# # Fjesboka
# 
# **Læringsmål:**
# 
# * Lister
# * Input
# * Strenger
# 
# **Starting Out with Python:**
# 
# * Kap. 7: Lists and Tuples
# * Kap. 8.3
#  * s. 379-380: Splitting a String
#  
# I denne oppgaven skal du ta inn informasjon fra brukere på et gitt format, lagre dataen i lister og gjøre det mulig for brukeren å hente ut denne informasjonen igjen. 

# ## a)

# Skriv en funksjon `add_data(user)` som skal ta inn en streng `user` på formatet: "given_name surname age gender relationship_status" og returnere dette i en liste.
# 
# Merk at alder skal lagres som en int, mens resten lagres som strenger. (Alder vil alltid ha indeks 2 i listen.)
# 
# **Eksempel på kjøring av kode**
# 
# >```python
# print(add_data("Mark Zuckerberg 32 Male Married"))
# skrives ut -> ["Mark", "Zuckerberg", 32, "Male", "Married"]```
# 
# ***Skriv koden din i kodeblokken under:***

# In[32]:


def main():
    facebook = []
    newUsr = "Mark Zuckerberg 32 male mArried"
    while not newUsr == 'exit':  
        facebook = addUser(newUsr, facebook)
        print(facebook)
        newUsr = str(input('\t\tGiven name + Surname + age + gender + marital status\nEnter new user: '))

def addUser(newUsr, lst):
    new = newUsr.split()
    new[2] = int(new[2])
    for i in[0,1,3,4]:
        new[i] = new[i].lower()
        new[i] = new[i].title()
    lst.append(new)
    return lst
    
main()


# #### Hint

# Den innebygde funksjonen `.split()` returnerer en liste bestående av ordene i en streng.

# ## b)

# Skriv en funksjon `get_person(given_name, facebook)` som tar inn et fornavn "given_name" og en liste "facebook" bestående av mange lister på formatet definert av `add_data(user)` og returnerer en liste bestående av alle personer med fornavnet **given_name.** 
# 
# >```python
# facebook = [["Mark", "Zuckerberg", 32, "Male", "Married"], 
#                 ["Therese", "Johaug", 28, "Female", "Complicated"],
#                 ["Mark", "Wahlberg", 45, "Male", "Married"],
#                 ["Siv", "Jensen", 47, "Female", "Single"]]
# print(get_person("Mark", facebook))
# skrives ut -> [["Mark", "Zuckerberg", 32, "Male", "Married"], ["Mark", "Wahlberg", 45, "Male", "Married"]]```
# 
# ***Skriv koden din i kodeblokken under:***

# In[18]:


def main():
    sList = []
    facebook = [["Mark", "Zuckerberg", 32, "Male", "Married"], 
                ["Therese", "Johaug", 28, "Female", "Complicated"],
                ["Mark", "Wahlberg", 45, "Male", "Married"],
                ["Siv", "Jensen", 47, "Female", "Single"]]
    
    print('[0] Exit | [1] Add new user | [2] Search for user | [3] Se everyone on facebook')
    choice = int(input('What do you want to do? '))
    while not choice == '0':  
        if choice == '1':
            facebook = setUsr(facebook)
            
        elif choice == '2':
            lookup = str(input('Who do you want to search for? '))
            sList = getUsr(lookup,facebook)
            print('\n')
            for i in range(0, len(sList)):
                print(sList[i])
        elif choice == '3':
            printAll(facebook)
        print('\n\n[0] Exit | [1] Add new user | [2] Search for user | [3] Se everyone on facebook')
        choice = str(input('What do you want to do now? '))

        
def setUsr(lst):
    print('\n\nType "done" to stop')
    newUsr = str(input('\t\tGiven name + Surname + age + gender + marital status\nEnter new user: '))
    while newUsr != 'done':
        new = newUsr.split()
        new[2] = int(new[2])
        for i in[0,1,3,4]:
            new[i] = new[i].lower()
            new[i] = new[i].title()
        lst.append(new)
        print('\n\nType "done" to stop')
        newUsr = str(input('\t\tGiven name + Surname + age + gender + marital status\nEnter new user: '))
    return lst

def getUsr(lookup,facebook):
    searchList = []
    lookup = lookup.title()
    for i in range(0,len(facebook)):
        if lookup in facebook[i]:
            searchList.append(facebook[i])
    if searchList == []:
        searchList = [f'{lookup} not on facebook.']
    return searchList

def printAll(facebook):
    print('\n')
    for i in range(0, len(facebook)):
        print(facebook[i])
    
    
main()


# Du kan teste ut funksjonen din med kodeblokken under, (men husk å kjøre kodeblokken din over som inneholder funksjonen først)

# In[ ]:


facebook = [["Mark", "Zuckerberg", 32, "Male", "Married"], 
                ["Therese", "Johaug", 28, "Female", "Complicated"],
                ["Mark", "Wahlberg", 45, "Male", "Married"],
                ["Siv", "Jensen", 47, "Female", "Single"]]
print(get_person("Mark", facebook))


# #### Hint

# Fornavnet (indeks = 0) på den første personen (indeks = 0) i listen `facebook` kan finnes ved å skrive `facebook[0][0]`.
# Det er mulig å iterere gjennom listen `facebook` i stedet for å bruke `facebook[m][n]`, der `m` og `n` er heltall.

# ## c)

# Skriv funksjonen **main()** som lar brukeren legge til flere personer i en liste.
# 
# Dette gjøres ved å be brukeren om å legge til en **user** på formen "given_name surname age gender relationship_status" så lenge svaret ikke er "done".
# 
# Disse skal legges inn i en liste **facebook** ved hjelp av funksjonen `add_data(user)`.
# 
# Hvis svaret er "done" blir brukeren sendt videre til neste steg. 
# 
# Deretter skal brukeren kunne printe ut informasjon om brukerene fra listen basert på fornavn ved hjelp av funksjonen `get_person(given_name)`. 
# 
# Hvis svaret er "done" er programmet ferdig.
# 
# (Du kan velge om du vil printe ut listene eller skrive en melding til brukeren som vist i eksempelet under)
# 
# Test programmet ved å kjøre **main()**. 
# 
# **Eksempel på kjøring av kode:**
# 
# >```
# Hello, welcome to Facebook. Add a new user by writing "given_name surname age gender relationship_status".
# Add a new user: Therese Johaug 29 Female Complicated
# Add a new user: Mark Zuckerberg 33 Male Married
# Add a new user: done
# Ok
# Search for a user: Therese
# Therese Johaug is 29 years old, her relationship status is Complicated.
# Search for a user: Alf
# []
# Search for a user: Mark
# Mark Zuckerberg is 33 years old, his relationship status is Married.
# Search for a user: done
# ```
# 
# ***Skriv koden din i kodeblokken under:***

# In[ ]:


def main():
    sList = []
    facebook = [["Mark", "Zuckerberg", 32, "Male", "Married"], 
                ["Therese", "Johaug", 28, "Female", "Complicated"],
                ["Mark", "Wahlberg", 45, "Male", "Married"],
                ["Siv", "Jensen", 47, "Female", "Single"]]
    print('Hello, welcome to Facebook.')
    print('[0] Exit | [1] Add new user | [2] Search for user | [3] Se everyone on facebook')
    choice = str(input('What do you want to do? '))
    while not choice == '0':  
        if choice == '1':
            facebook = setUsr(facebook)   
        elif choice == '2':
            getUsr(facebook)
        elif choice == '3':
            printAll(facebook)
        print('\n\n[0] Exit | [1] Add new user | [2] Search for user | [3] Se everyone on facebook')
        choice = str(input('What do you want to do now? '))

        
def setUsr(lst):
    print('\n\nType "done" to stop')
    newUsr = str(input('\t\tGiven name + Surname + age + gender + marital status\nEnter new user: '))
    while newUsr != 'done':
        new = newUsr.split()
        new[2] = int(new[2])
        for i in[0,1,3,4]:
            new[i] = new[i].lower()
            new[i] = new[i].title()
        lst.append(new)
        print('\n\nType "done" to stop')
        newUsr = str(input('\t\tGiven name + Surname + age + gender + marital status\nEnter new user: '))
    return lst

def getUsr(facebook):
    lookup = str(input('Who do you want to search for? '))
    searchList = []
    lookup = lookup.title()
    
    for i in range(0,len(facebook)):
        if lookup in facebook[i]:
            searchList.append(facebook[i])
    print('\n')
    if searchList == []:
        searchList = [f'{lookup} not on facebook.']
    for i in range(0, len(searchList)):
        if searchList[i][3] == 'Male' or searchList[i][3] == 'M':
            print(f'{searchList[i][0]} {searchList[i][1]} is {searchList[i][2]} years old, and his marital status is {searchList[i][4].lower()}')
        elif searchList[i][3] == 'Female' or searchList[i][3] == 'F':
            print(f'{searchList[i][0]} {searchList[i][1]} is {searchList[i][2]} years old, and her marital status is {searchList[i][4].lower()}')

def printAll(facebook):
    print('\n')
    for i in range(0, len(facebook)):
        print(facebook[i])
    
    
main()


# In[ ]:


"""
Just for fun:
Facebook with i/o to binary-file for later use of vector

!!! Requirements !!!
Requires an IDLE with pickle and os.path installed (ie. not working on Jupyter)
Requires access to path in which the .py file is located. 
"""


import pickle
import os.path

def main():
    """
    Init vectors and strings:
    """
    
    if not os.path.exists('facebook.data'): # Initiate file with a few datapoints if file not exist
        open('facebook.data','w+')
        facebook = [["Mark", "Zuckerberg", 32, "Male", "Married"], 
                ["Therese", "Johaug", 28, "Female", "Complicated"],
                ["Mark", "Wahlberg", 45, "Male", "Married"],
                ["Siv", "Jensen", 47, "Female", "Single"]]
        with open('facebook.data','wb') as fb: # Dumping initial datapoints to file
            pickle.dump(facebook, fb)    
    with open('facebook.data','rb') as fb: # Load existing datapoints into facebook vector
        facebook = pickle.load(fb)
    sList = []

    print('Hello, welcome to Facebook.')
    print('[0] Exit | [1] Add new user | [2] Search for user | [3] Se everyone on facebook')
    choice = str(input('What do you want to do? '))
    while not choice == '0': #Exit
        if choice == '1': #Add user
            facebook = getFromFB()
            facebook = setUsr(facebook)
            sendToFB(facebook)
        elif choice == '2': #Search for user
            facebook = getFromFB()
            getUsr(facebook)
        elif choice == '3': #Print all
            printAll(facebook)
        print('\n\n[0] Exit | [1] Add new user | [2] Search for user | [3] Se everyone on facebook')
        choice = str(input('What do you want to do now? '))

        
def setUsr(lst):
    print('\n\nType "done" to stop')
    newUsr = str(input('\t\tGiven name + Surname + age + gender + marital status\nEnter new user: '))
    while (newUsr != 'done'):
        new = newUsr.split()
        new[2] = int(new[2])
        for i in[0,1,3,4]:
            new[i] = new[i].lower()
            new[i] = new[i].title()
        lst.append(new)
        print('\n\nType "done" to stop')
        newUsr = str(input('\t\tGiven name + Surname + age + gender + marital status\nEnter new user: '))
    return lst

def getUsr(facebook):
    lookup = str(input('Who do you want to search for? '))
    searchList = []
    gender = ""
    lookup = lookup.title()
    
    for i in range(0,len(facebook)):
        if lookup in facebook[i]:
            searchList.append(facebook[i])
    print('\n')
    if searchList == []:
        searchList = [f'{lookup} not on facebook.']
    for i in range(0, len(searchList)):
        gender = searchList[i][3]
        if gender[0] == 'M':
            print(f'{searchList[i][0]} {searchList[i][1]} is {searchList[i][2]} years old, and his marital status is {searchList[i][4].lower()}')
        elif gender[0] == 'F':
            print(f'{searchList[i][0]} {searchList[i][1]} is {searchList[i][2]} years old, and her marital status is {searchList[i][4].lower()}')

def printAll(facebook): # Print all datapoints in file
    fbRead = []
    print('\n')
    with open('facebook.data','rb') as fb:
        fbRead = pickle.load(fb)
    for i in range(0, len(fbRead)):
        print(fbRead[i])

def sendToFB(facebook): # Send all datapoints to file
    with open('facebook.data','wb') as fb:
        pickle.dump(facebook, fb)

def getFromFB(): # Load all datapoints from file
    fbTemp = []
    with open('facebook.data','rb') as fb:
        fbTemp = pickle.load(fb)
    return fbTemp
    
main()

