alt1 = 'åpne døren'
alt2 = 'snu'
alt3 = 'bank på'
alt4 = 'se under dørmatta'
alt5 = 'exit'
answers = [alt1, alt2, alt3, alt4, alt5]
ans = ""
key = False

while (ans != alt1) or (key == False):
    print("Du står utenfor en dør.")
    ans = input("Hva gjør du? ").lower()
    
    
    while (not ans in answers):
        print("Forstår ikke kommando, prøv noe annet\nDu står utenfor en dør.")
        ans = input("Hva gjør du? ").lower()
    
    
    if (ans == alt1 and key == False):
        print("Døren er låst")
    elif (ans == alt2):
        print("Du snur deg og vandrer hjem igjen. Du hører en skummel lyd og løper tilbake.")
    elif (ans == alt3):
        print("Du får ingen respons.")
    elif (ans == alt4):
        print("Du finner en nøkkel, og låser opp døren.")
        key = True
    elif (ans == alt5):
        print("Ha en fin dag")
        break
    
