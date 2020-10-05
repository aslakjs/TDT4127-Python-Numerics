#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving2.ipynb">Øving 2</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li class="active"><a href="Ulike%20typer%20if-setninger.ipynb">Ulike typer if-setninger</a></li>
#     <li><a href="Sammenligning%20av%20strenger.ipynb">Sammenligning av strenger</a></li>
#     <li><a href="Logiske%20operatorer%20og%20logiske%20uttrykk.ipynb">Logiske operatorer og logiske uttrykk</a></li>
#     <li><a href="Forbrytelse%20og%20straff.ipynb">Forbrytelse og straff</a></li>
#     <li><a href="Aarstider.ipynb">Årstider</a></li>
#     <li ><a href="Tekstbasert%20spill.ipynb">Tekstbasert spill</a></li>
#     <li><a href="Sjakkbrett.ipynb">Sjakkbrett</a></li>
#     <li><a href="Billettpriser%20og%20rabatter.ipynb">Billettpriser og rabatter</a></li>
#     <li><a href="Skatteetaten.ipynb">Skatteetaten</a></li>
#     <li><a href="Epletigging.ipynb">Datamaskinen som tigget epler</a></li>
#     <li><a href="Andregradsligning.ipynb">Andregradsligning</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Ulike typer if-setninger
# 
# **Læringsmål:**
# 
# - Betingelser
# 
# **Starting Out with Python:**
# 
# - Kap. 3.1- 3.2
# - Kap. 3.4

# ## Generelt om if-setninger
# Dette er ikke en del av oppgaven, men kan være lurt å lese før du begynnner. **Trykk på pilen til venstre for å lese**

# I oppgavene i øving 1 har det vært slik at alle setningene i programmet skulle utføres hver gang programmet kjørte. De fleste nyttige programmer er ikke så enkle. Ofte skal visse programsetninger kun utføres under gitte betingelser. Overtidslønn skal utbetales bare hvis det har vært jobbet overtid. Monsteret du kjemper mot i et spill, skal miste liv bare hvis skuddet eller sverdslaget ditt har truffet. En alarm skal aktiveres bare hvis pasientens hjerterytme er blitt unormal. En sosial app på mobilen skal gi et spesielt varsel bare hvis du har fått nye meldinger der. Kodeblokken nedenfor viser et eksempel hvor alle linjene blir utført - dette programmet vil anbefale paraply uansett hvordan været er.

# In[ ]:


regn = float(input("Hvor mange mm regn er det meldt? "))
print("Da anbefaler jeg paraply!")
print("Ha en fin tur til universitetet!")


# Paraply bør anbefales bare ved behov, f.eks. hvis det var meldt mer enn 0.2 mm regn. Det oppnår vi med en if-setning:

# In[ ]:


regn = float(input("Hvor mange mm regn er det meldt? "))
if regn > 0.2:
    print("Da anbefaler jeg paraply!")
print("Ha en fin tur til universitetet!")


# Den ovenstående kodeblokken viser en if-setning. Den har følgende struktur:
# 
# - starter med ordet `if`, dette er et beskyttet ord i Python og kan derfor ikke brukes som variabelnavn e.l.
# - bak if kommer en logisk betingelse - i dette tilfellet `regn > 0.2` - som vil være enten sann (`True`) eller usann (`False`), her avhengig av innholdet i variabelen regn
# - bak betingelsen **må** if-setningen ha `:` **(kolon)** - hvis du glemmer kolon vil du få syntaksfeil. 
# - kodelinjen like under if har et innrykk (tabulator), dette betyr at denne linjen - `print("Da anbefaler jeg paraply")` - er del av if-setningen. Den vil bli utført **kun hvis betingelsen i if-setningen er sann**, som vil inntreffe hvis brukeren skriver inn et større tall enn 0.2
# 
# Siste setning, `print("Ha en fin tur til universitetet!")` , har derimot ikke innrykk, denne vil derfor bli utført uansett og er ikke knyttet til if-setningen.
# 
# 

# Det er mulig å ha flere programsetninger som del av if-setningen, for eksempel:

# In[ ]:


regn = float(input("Hvor mange mm regn er det meldt? "))
if regn > 0.2:
    print("Da anbefaler jeg paraply!")
    print("Gjerne en paraply med NTNU-logo.")
print("Ha en fin tur til universitetet!")


# Her vil begge "print"-setningene om paraply kun bli utført hvis betingelsen er sann, mens "fin tur"-setningen fortsatt blir utført uansett utfall av if-setningen.
# 
# **Altså: I Python viser innrykk hvor mange av de påfølgende setningene som styres av if-betingelsen.** Det er derfor viktig å være nøye med innrykkene og få alle programsetninger på korrekt indentasjonsnivå.
# 
# Test gjerne ut koden over med forskjellige svar på mm regn for å se hvordan den virker.

# ## a)

# Du lager en banankake som skal stå minst 50 min i ovnen. Ta utgangspunkt i følgende program, som har den svakheten at det sier at kaken skal ut uansett hvor lenge den har stekt.
# 
# ___Endre programmet slik at "Kaken kan tas ut av ovnen" kun printes hvis kaken har stått minst 50 minutt. "Større eller lik" skrives i Python >=___  
# ___Tips til servering... skal derimot printes uansett.___

# In[6]:


tid = int(input("Hvor mange minutt har kaken stått i ovnen? "))
if tid >= 65:
    print("Kaken er brent, du må lage ny.")
elif tid >= 50:
    print("Kaken kan tas ut av ovnen.")
else:
    print(f'Kaken er ferdig om {50-tid} minutter.')
print("Tips til servering: vaniljeis.")


# Eksempel på utskrift fra tre ulike kjøringer, hvis du har fått det til riktig:
# ```
# Hvor mange minutt har kaken stått i ovnen? 35  
# Tips til servering: vaniljeis.  
# >>>  
#   
# Hvor mange minutt har kaken stått i ovnen? 50  
# Kaken kan tas ut av ovnen.  
# Tips til servering: vaniljeis.  
# >>>
#   
# Hvor mange minutt har kaken stått i ovnen? 65  
# Kaken kan tas ut av ovnen.  
# Tips til servering: vaniljeis.
# >>>
# ```

# ## b)

# Ta utgangspunkt i følgende program, som ber brukeren taste inn antall epler og antall barn og deretter regner ut hvor mange epler det blir på hver.

# In[8]:


epler = int(input("Hvor mange epler har du? "))
barn = int(input("Hvor mange barn passer du? "))

if barn > 0:
    print("Da blir det", epler // barn, "epler til hvert barn")
    print("og", epler % barn, "epler til overs til deg selv.")
else:
    print('Da får du alle {0} eplene selv! :D'.format(epler))
print("Takk for i dag!")


# Under vises to kjøreeksempler:
# ```
# Hvor mange epler har du? 14  
# Hvor mange barn passer du? 3  
# Da blir det 4 epler til hvert barn  
# og 2 epler til overs til deg selv.  
# Takk for i dag!
# >>>>```
#   
# ```
# Hvor mange epler har du? 4  
# Hvor mange barn passer du? 0  
# Traceback (most recent call last):  
#   ...  
# ZeroDivisionError: integer division or modulo by zero  
# >>>```
# 
# 
# Det første, hvor brukeren skriver inn tallene 14 og 3, funker fint. Hvis brukeren derimot svarer 0 barn, vil programmet gi feilmelding (`ZeroDivisionError`) fordi det er umulig å dele på null. Negativt antall barn vil "funke", men ikke gi mening.
# 
# ___Endre koden slik at de to print-setningene som forteller hvor mange epler det blir til barna og deg selv KUN utføres hvis barn > 0. "Takk for i dag!" skal derimot printes uansett.___
# 
#  Kjøring med barn > 0 skal gi samme resultat som eksemplet øverst. Eksemplet under viser kjøring hvis det skrives 0 for barn:
#  
#  ```
# Hvor mange epler har du? 4  
# Hvor mange barn passer du? 0  
# Takk for i dag!
# ```
#  

# ## Generelt om if-else-setninger
# Dette er ikke en del av oppgaven, men kan være lurt å lese før du går videre. **Trykk på pilen til venstre for å lese**

# I eksemplene knyttet til (a) og (b) skulle vi gjøre noe ekstra hvis en betingelse var sann, ellers la være. I andre tilfeller kan vi ønske å gjøre en handling hvis betingelsen er sann, og en alternativ handling hvis den er usann.
# 
# Det kan vi oppnå med en **if-else**-setning. Eksemplet nedenfor bygger videre på tilsvarende eksempel for if-setninger.

# In[ ]:


regn = float(input("Hvor mange mm regn er det meldt? "))
if regn > 0.2:
    print("Da anbefaler jeg paraply!")
    print("Gjerne en paraply med NTNU-logo.")
else:
    print("Hva med ei T-skjorte med NTNU-logo?")
print("Ha en fin tur til universitetet!")


# I dette eksemplet vil følgende skje hvis vi svarer mer enn 0.2 mm nedbør slik at betingelsen blir sann:
# 
# **Eksempel på kjøring med over 0.2 mm nedbør:**
# ```
# Hvor mange mm regn er det meldt? 0.5
# Da anbefaler jeg paraply!
# Gjerne en paraply med NTNU-logo.
# Ha en fin tur til universitetet!
# ```
# 
# Svares det derimot et lavere tall, slik at betingelsen blir usann, skjer følgende:
# 
# **Eksempel på kjøring med under 0.2 mm nedbør:**  
# ```
# Hvor mange mm regn er det meldt? 0.0
# Hva med ei T-skjorte med NTNU-logo?
# Ha en fin tur til universitetet!
# ```
# 
# Altså:
# - De to setningene som står på innrykk under `if` blir utført bare hvis betingelsen er sann.
# - Setningen som står på innrykk under `else` blir utført bare hvis betingelsen er usann (kunne også hatt flere setninger på innrykk etter `else`).
# - Den siste printen, som ikke har innrykk (Ha en fin tur...), blir utført uansett.

# ## c)

# I denne deloppgaven skal det lages et program som sjekker om en person kan stemme, altså om personen er 18 år eller eldre. Man må da spørre brukeren om alder og lagre svaret i en variabel, for deretter å sjekke om brukerens alder er 18 eller mer.
# 
# **Eksempel på kjøring**
# 
# ```
# Skriv inn din alder: 19
# Du kan stemme:)
# ```
#   
# ```
# Skriv inn din alder: 18
# Du kan stemme:)
# ```
#   
# ```
# Skriv inn din alder: 2
# Du kan ikke stemme ennå
# ```
# 
# ***Skriv din kode her:***

# In[10]:


age = int(input('din alder: '))

if age >= 18:
    print('stem i vei')
else:
    print('voks opp')


# #### Fremgangsmåte
# Trykk på pilen til venstre for å lese

# 1. Lag en variabel kalt `alder` ved å skrive: 
# 2. `alder = int(input("Skriv inn din alder: "))`
# 3. Sjekk, vha. if, om personens alder er større eller lik 18 (`alder >= 18`). Om dette er tilfelle skal "Du kan stemme:)" skrives ut til skjerm
# Lag en `else`-blokk med koden `print("Du kan ikke stemme ennå")`
# 
# (Det er flere mulige løsninger på denne oppgaven.)

# ## Generelt om if-elif-else-setninger
# Les gjerne denne før du går videre. **Trykk på pilen til venstre for å lese**

# I eksemplene vi har sett hittil, har det vært kun to mulige utfall på betingelsene - kaken har stått >= 50 minutt, eller ikke; antall barn er > 0, eller ikke; alder er over 18, eller ikke. I mange praktiske situasjoner kan det være tre eller flere mulige utfall.
# 
# F.eks. hvis det var meldt mer enn 3 mm nedbør er kanskje ikke paraply tilstrekkelig, vi ville heller anbefale støvler og regntøy.  Vårt tidligere eksempel kunne da utvides som følger:

# In[ ]:


# EKSEMPEL 1
regn = float(input("Hvor mange mm regn er det meldt? "))
if regn > 3.0:
    print("Da anbefaler jeg støvler og regntøy!")
elif regn > 0.2:
    print("Da anbefaler jeg paraply!")
    print("Gjerne en paraply med NTNU-logo.")
else:
    print("Hva med ei T-skjorte med NTNU-logo?")
print("Ha en fin tur til universitetet!")


# Under vises tre kjøringer av denne koden:
# 
# ```
# Hvor mange mm regn er det meldt? 4.2
# Da anbefaler jeg støvler og regntøy!
# Ha en fin tur til universitetet!
# >>>
# ```
# 
# ```
# Hvor mange mm regn er det meldt? 0.5
# Da anbefaler jeg paraply!
# Gjerne en paraply med NTNU-logo.
# Ha en fin tur til universitetet!
# >>>
# ```
# 
# ```
# Hvor mange mm regn er det meldt? 0.0
# Hva med ei T-skjorte med NTNU-logo?
# Ha en fin tur til universitetet!
# ```

# Hvis betingelsen `regn > 3.0` er sann, utføres kun printen som anbefaler støvler og regntøy, deretter går programmet til første setning etter hele if-elif-else-setningen ("Ha en fin tur...")
# 
# Hvis betingelsen `regn > 3.0` er usann, utføres **ikke** printen om støvler, programmet sjekker i stedet betingelsen på `elif`. Hvis denne er sann, skrives setningene om paraply, ellers T-skjorte som tidligere.
# 
# Det er mulig å klare seg uten if-elif-else-setninger og i stedet bare putte if-else-setninger inni hverandre for å oppnå det samme. Eksemplet ovenfor kunne alternativt skrives:

# In[ ]:


# EKSEMPEL 2
regn = float(input("Hvor mange mm regn er det meldt? "))
if regn > 3.0:
    print("Da anbefaler jeg støvler og regntøy!")
else:
    if regn > 0.2:
        print("Da anbefaler jeg paraply!")
        print("Gjerne en paraply med NTNU-logo.")
    else:
        print("Hva med ei T-skjorte med NTNU-logo?")
print("Ha en fin tur til universitetet!")


# Særlig i tilfeller hvor det dreier seg om tre eller flere alternative utfall basert på verdien av den **samme variabelen** (f.eks. `regn` her) vil de fleste oppfatte **if-elif-else**-setninger som både lettere å skrive og lettere å forstå, enn flere nøstede if-else-setninger.
# 
# Ett typisk eksempel er antall oppnådde poeng på en eksamen, som kan transformeres til en bokstavkarakter A-F etter gitte grenser. Det er da 6 mulige utfall, dette gir mye innrykk og blir vanskelig å lese med nøstede if-setninger:

# In[ ]:


# EKSEMPEL 3
score = int(input("Antall poeng: "))
  
if score >= 89:
    karakter = "A"
else:
    if score >= 77:
        karakter = "B"
    else:
        if score >= 65:
            karakter = "C"
        else:
            if score >= 53:
                karakter = "D"
            else:
                if score >= 41:
                    karakter = "E"
                else:
                    karakter = "F"
  
print("Du fikk", karakter)


# if-elif-else-setning vil være klart å foretrekke i en slik situasjon; det er mye lettere å se at koden her tar en beslutning med 6 alternativer basert på verdien av en enkelt variabel:

# In[ ]:


# EKSEMPEL 4
score = int(input("Antall poeng: "))
  
if score >= 89:
    karakter = "A"
elif score >= 77:
    karakter = "B"
elif score >= 65:
    karakter = "C"
elif score >= 53:
    karakter = "D"
elif score >= 41:
    karakter = "E"
else:
    karakter = "F"
 
print("Du fikk", karakter)


# Ved bruk av if-elif-else er det avgjørende at betingelsene kommer i riktig rekkefølge. Anta at vi hadde gjort karaktereksemplet motsatt:

# In[ ]:


# EKSEMPEL 5
# HER HAR VI MED VILJE HAR GJORT FEIL
score = int(input("Antall poeng: "))
 
if score >= 0:
    karakter = "F"
elif score >= 41:
    karakter = "E"
elif score >= 53:
    karakter = "D"
elif score >= 65:
    karakter = "C"
elif score >= 77:
    karakter = "B"
elif score >= 89:
    karakter = "A"
 
print("Du fikk", karakter)


# Her vil øverste betingelse vil være sann for alle eksamensbesvarelser - og alle ender opp med karakteren F.
# 
# Det er også viktig når det er snakk om alternativt ekskluderende utfall av samme beslutning at vi bruker **if-elif-else**-setning; **IKKE en serie med frittstående if-setninger**.
# 
# Eksempel 6 under ser nesten ut som Eksempel 4, bare at vi kun skriver `if` der vi før skrev `elif`:

# In[ ]:


# EKSEMPEL 6
# HER HAR VI MED VILJE HAR GJORT FEIL
score = int(input("Antall poeng: "))
  
if score >= 89:
    karakter = "A"
if score >= 77:
    karakter = "B"
if score >= 65:
    karakter = "C"
if score >= 53:
    karakter = "D"
if score >= 41:
    karakter = "E"
else:
    karakter = "F"
 
print("Du fikk",karakter)


# En student som har fått 92 poeng vil her komme riktig ut av den første if-setningen, og karakter settes til A. Men 92 > 77 er også sant, så karakter omgjøres deretter til B. Så til C, så til D, så til E.
# 
# De eneste tilfellene som dette programmet vil takle korrekt blir dermed studenter som skal ha E eller F.
# 
# Feilen her er at vi bruker nye frittstående if-setninger (dvs. som ikke er relatert til hverandre), mens vi egentlig har å gjøre med gjensidig ekskluderende alternativer som skulle vært løst med if-elif-else.
# 
# Hvor er det eventuelt riktig å bruke frittstående if-setninger? Jo, hvis det er snakk om flere uavhengige beslutninger. I eksempel 7 under er det to uavhengige beslutninger, den ene om man skal ta paraply eller ikke, den andre om brodder eller ikke. Hver beslutning tas uavhengig av den andre, da blir det riktig med to frittstående if-setninger.
# 
# Hadde vi i stedet brukt if-elif her, ville programmet ikke ha virket som det skulle, da det kun ville ha vært i stand til å anbefale brodder i oppholdsvær (mens det jo kan være minst like glatt om det regner).

# In[ ]:


# EKSEMPEL 7
regn = float(input("Hvor mange mm regn er det meldt? "))
glatt = int(input("Hvor glatt er det, fra 0 (ikke) til 10 (blank is)? "))
if regn > 0.2:
    print("Da anbefaler jeg paraply.")
if glatt > 8:
    print("Da anbefaler jeg sko med brodder eller pigger.")


# I andre tilfeller kan en beslutning være avhengig av en annen, f.eks. kun være aktuell ved et visst utfall av en foregående if-setning. Som i eksempel 8 under:

# In[ ]:


# EKSEMPEL 8
regn = float(input("Hvor mange mm regn er det meldt? "))
vind = float(input("Hvor mange m/s vind er det meldt? "))
if regn > 0.2:
    if vind < 7.0:
        print("Da anbefaler jeg paraply.")
    else:
        print("Anbefaler regntøy, for mye vind for paraply.")


# Her ville if `regn > 0.2:` .....`elif vind < 7.0` ha blitt feil.
# 
# Programmet ville da ha gjort vurderinger av vinden kun hvis det ikke regnet, og dermed ha vært ute av stand til å fraråde paraply hvis det regner og samtidig blåser kraftig.
# 
# **Oppsummert:**
# 
# - flere helt uavhengige beslutninger: bruk frittstående if-setninger
# - beslutning med gjensidig utelukkende handlingsalternativer: bruk if-else (2 alternativer) eller if-elif-else (3 eller flere alternativer)
# - beslutninger relatert på annen måte, f.eks. at en betingelse (som `vind < 7.0` ovenfor) kun er aktuell gitt et visst utfall av en annen betingelse: kan løses ved å nøste flere if-setninger inni hverandre
# 

# ## d)

# Lag en utvidet versjon av programmet fra (c) som sier om personen kan stemme eller ikke, med følgende regler:
# 
# - `alder >= 18`: Kan stemme både ved lokalvalg og Stortingsvalg
# - `alder >= 16`: Kan stemme ved lokalvalg, men ikke ved Stortingsvalg
# - ellers (`alder < 16`): Kan ikke stemme.
# 
# Eksempel på kjøring:
# 
# ```
# Skriv inn din alder: 19
# Du kan stemme både ved lokalvalg og Stortingsvalg
# >>>>
# ```
# 
# ```
# Skriv inn din alder: 17
# Du kan stemme ved lokalvalg, men ikke ved Stortingsvalg
# >>>>
# ```
# 
# ```
# Skriv inn din alder: 12
# Du kan ikke stemme ennå
# ```
# 
# ___Skriv din kode her:___

# In[ ]:


age = int(input('din alder: '))

if age >= 18:
    print('stem i vei, både på lokal- og stortingsvalg')
elif age >= 16:
    print('stem i vei, men bare på lokalvalg')
else:
    print('voks opp')


# ## e)

# Du skal lage et program som sjekker hvilken billettpris en person skal betale ut ifra alderen til personen.
# 
# Oversikt over alder og tilhørende billettpriser:
# 
# Aldersgruppe | Billettpris
# --- | ---
# Under 3 år | Gratis
# 3-11 år | 30 kr
# 12-25 år | 50 kr
# 26-66 år | 80 kr
# 67 år og over | 40 kr

# ___Skriv din kode her:___

# In[1]:


age = 1
while age != 0:
    age = int(input('din alder: '))
        
    if age >= 67:
        print('betal 40kr')
    elif age >= 26:
        print('betal 80kr')
    elif age >= 12:
        print('betal 50kr')
    elif age >= 3:
        print('betal 30kr')
    else:
        print('gratis')


# #### Fremgangsmåte
# Trykk på pilen til venstre

# 1. Først må man ta inn alderen til personen. Dette gjøres ved å lage en variabel og ta inn input fra brukeren: `alder = int(input("Din alder: "))`
# 2. Videre skal man sjekke hvilken billett personen skal ha, og dette gjøres med en if-elif-else-setning:
# 
# ```
# if alder < 3:
#   ...
# elif alder < 12:
#   ...
# elif ...:
#   ...
# elif ...:
#   ...
# else:
#   ...
# ```
