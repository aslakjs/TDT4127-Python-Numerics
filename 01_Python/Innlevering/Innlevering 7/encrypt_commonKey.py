import easygui  # Uncomment for error-mbox (Not working on Jupyter)
import binascii
from random import randint
from time import sleep
import pickle
import os.path

def main():
    """
    Init vectors and strings:
    """
    if not os.path.exists('cryptKey.data'):
        open('cryptKey.data','w+')
        with open('cryptKey.data','wb') as keySave:
            pickle.dump(keyGen(1000), keySave)    
    with open('cryptKey.data','rb') as keyS:
        key = pickle.load(keyS)

                  
    if not os.path.exists('wordlist.data'):
        open('wordlist.data','w+')
        wList = []
    else:
        with open('wordlist.data','rb') as wordlist:
            wList = pickle.load(wordlist)
    print(wList)

    """
    Encrypt message:
    Encryption takes inn new message, and if not in updated wList -> add
    """
    message = str(input('Enter your secret message: '))
    while message != 'exit':
        secret  = ''
        mList   = []
        sList   = []
        
        if ' ' in message:
            mList = message.split()
            for i in range (0,len(mList)):
                sList.append(encrypt(mList[i],key))
                secret = secret + ' ' + str(sList[i])
                if mList[i] not in wList:
                    add2wList(mList[i],sList[i],wList)
        else:
            secret = str(encrypt(message,key))
            if not secret in wList:
                add2wList(message,secret,wList)

        sleep(2)
        """
        Decrypt message:
        Decryption has access to wList and the secret for the message
        """
        rmsg = decrypt(secret, wList)
        #print('Encoded:\t',secret)
        #print('Key:\t\t',key)
        #print(wList)
        print('Message:\t',rmsg)
        
        # New message:
        message = ''
        message = str(input('Enter your secret message: '))
    
    
# Encryption
def encrypt(msg, key):
    xkey = ''
    if len(key) != len(msg):
        for i in range(0,len(msg)):
            xkey = key + key[i]
    else:
        xkey = key
    msg = toHex(bytes(msg, encoding = 'ascii'))
    xkey = toHex(bytes(key, encoding = 'ascii'))
    return xkey^msg

def add2wList(msg,encode,wList):
    wList.append(msg)
    wList.append(encode)
    with open('wordlist.data','wb') as wordlist:
        pickle.dump(wList, wordlist)
    return wList
    
def keyGen(length):
    key = ''
    for p in range(0,length):
        key += str(randint(0,9))
        p += 1
    return key


# Common functions:
def toHex(word):
    return int(str(binascii.hexlify(word), 'ascii'), 16)
def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')
def perror(err):
    easygui.msgbox(err, title="ERROR")



    
# Decryption: 
def decrypt(secret, wList):
    sList = []
    msg = ''
    if ' ' in secret:
        sList = secret.split()
        print(sList)
        for d in range(0,len(sList)):
            p = wList.index(sList[d])
            print(wList[p])
            msg = msg + ' ' + wList[p-1]
    else:
        p = wList.index(secret)
        print(wList[p])
        msg = wList[p-1]
    
    return msg

main()


