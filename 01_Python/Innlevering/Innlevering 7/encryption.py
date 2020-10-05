import easygui
import binascii
from random import randint

def main():
    message = str(input('Enter your secret message: '))
    key     = keyGen(message)
    secret = encrypt(message,key)
    if not secret:
         perror('Unable to encrypt')
    else:
        rmsg = decrypt(secret,key)
        print('Encoded:\t',secret)
        print('Key:\t\t',key)
        print('Message:\t',rmsg)
    
    
# Encryption
def encrypt(msg, key):
    if len(key) != len(msg):
        return False
    msg = toHex(bytes(msg, encoding = 'ascii'))
    key = toHex(bytes(key, encoding = 'ascii'))
    return key^msg

def keyGen(msg):
    key = ''
    for p in range(0,len(msg)):
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
def decrypt(secret, key):
    key = toHex(bytes(key, encoding = 'ascii'))
    return toString(secret^key)


main()
