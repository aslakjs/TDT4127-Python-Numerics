import pickle
import os.path

def main():
    """
    Init vectors and strings:
    """
    
    if not os.path.exists('facebook.data'):
        open('facebook.data','w+')
        facebook = [["Mark", "Zuckerberg", 32, "Male", "Married"], 
                ["Therese", "Johaug", 28, "Female", "Complicated"],
                ["Mark", "Wahlberg", 45, "Male", "Married"],
                ["Siv", "Jensen", 47, "Female", "Single"]]
        with open('facebook.data','wb') as fb:
            pickle.dump(facebook, fb)    
    with open('facebook.data','rb') as fb:
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

def printAll(facebook):
    fbRead = []
    print('\n')
    with open('facebook.data','rb') as fb:
        fbRead = pickle.load(fb)
    for i in range(0, len(fbRead)):
        print(fbRead[i])

def sendToFB(facebook):
    with open('facebook.data','wb') as fb:
        pickle.dump(facebook, fb)

def getFromFB():
    fbTemp = []
    with open('facebook.data','rb') as fb:
        fbTemp = pickle.load(fb)
    return fbTemp
    
main()
