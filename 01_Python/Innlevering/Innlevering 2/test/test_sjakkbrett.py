while True:
    usr = str(input('Skriv inn en posisjon: '))
    pos = str(usr.lower())
    if pos == 'exit':
        break
    
    ex = False
    while ex == False:
        pos = pos + str('  ')
    
        if ((pos[1] == str(' ')) or (pos[2] != str(' '))):
            print('Feil input.')
            usr = str(input('Skriv inn en korrekt posisjon: '))
            pos = str(usr.lower())
            
        elif (pos[0] != 'a') and (pos[0] != 'b') and (pos[0] != 'c') and (pos[0] != 'd') and (pos[0] != 'e') and (pos[0] != 'f') and (pos[0] != 'g') and (pos[0] != 'h'):
            print('Første tegn må være en bokstav A-H eller a-h')
            usr = str(input('Skriv inn en korrekt posisjon: '))
            pos = str(usr.lower())
            
        if (pos[1] != '1') and (pos[1] != '2') and (pos[1] != '3') and (pos[1] != '4') and (pos[1] != '5') and (pos[1] != '6') and (pos[1] != '7') and (pos[1] != '8'):
            print('Andre tegn må være et tall 1-8')
            usr = str(input('Skriv inn en korrekt posisjon: '))
            pos = str(usr.lower())
            
        else:
            ex = True


            
    b = pos[0]              #gir variabelen bokstav-verdi
    t = int(pos[1])         #gir variabelen tall-verdi 
    
    if ((b == 'a') or (b == 'c') or (b == 'e') or (b == 'g')):
        if (t % 2 != 0):    # Hvis oddetall
            print('black')
        else:
            print('white')
    
    elif ((b == 'b') or (b == 'd') or (b == 'f') or (b == 'h')):
        if (t % 2 != 0): 
            print('white')
        else:
            print('black')
