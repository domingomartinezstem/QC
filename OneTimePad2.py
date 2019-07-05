# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:50:24 2019

@author: domin
"""

import random
import numpy as np
import string

string.ascii_letters

s=input("Please enter your plaintext: ")
#create empty arrays to but in ascii value and random key
encrypt=[]
key=[]
h=""
t=""
xOR=""
for letter in s:
    l=ord(letter)
    #choose a random letter
    w=ord(random.choice(string.ascii_letters))
    #convert to binary
    binaryW=int(bin(w)[2:])
    binaryL=int(bin(l)[2:])
    #convert to a string
    strW=str(binaryW)
    strL=str(binaryL)
    h += strW
    t += strL
    encrypt.append(binaryL)
    key.append(binaryW)
print(encrypt)
print(key)

v_key=[]
v_message=[]
for i in h:
    v_key.append(i)

for i in t:
    v_message.append(i)

#encrpyt 
v_xOR=[]
for i in range(len(v_key)):
        if v_key[i]=='1' and v_message[i] =='1':
            b='0'
        if v_key[i]=='0' and v_message[i]== '0':
            b='0'
        if v_key[i]=='1' and v_message[i]=='0':
            b='1'
        if v_key[i]=='0' and v_message[i]=='1':
            b='1'
        xOR += b
for i in xOR:
    #u2=int(i)
    v_xOR.append(i)
#decrypt
decrypt=""
for i in range(len(v_message)):
        if v_key[i]=='1' and v_xOR[i] =='1':
            b2='0'
        if v_key[i]=='0' and v_xOR[i]== '0':
            b2='0'
        if v_key[i]=='1' and v_xOR[i]=='0':
            b2='1'
        if v_key[i]=='0' and v_xOR[i]=='1':
            b2='1'
        decrypt+=b2
        
v_decrypt=[]
for i in decrypt:
    n=int(i)
    v_decrypt.append(n)

v_Decrypt=np.reshape(v_decrypt,(len(v_decrypt),1))
dmessage=np.concatenate(v_Decrypt)

spaceMessage= np.array_split(dmessage, len(s))

decrpyted_message=""
for i in spaceMessage: 
    xy=str(i)
    xy=xy.replace(' ','')
    xy=xy.replace('[','')
    xy=xy.replace(']','')
    xY=int(xy,2)
    LL=chr(xY)
    decrpyted_message += LL
    
print()
print("encrypted message: " + h)
print("key text:          " + t)
print("xor     :          " + xOR)
print()
print("decrypt xor:       " + decrypt)
print()
print("decrypted message: " + decrpyted_message)


