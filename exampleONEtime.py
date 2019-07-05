# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:48:07 2019

@author: domin
"""
import random
import string

string.ascii_letters

let=input("type a letter: ")
letter=ord(let)
random_letter=ord(random.choice(string.ascii_letters))
print(letter)
print(random_letter)
print()
#convert to binary
binaryL=int(bin(letter)[2:])
binarykey=int(bin(random_letter)[2:])
print(binaryL)
print(binarykey)
print()
#convert to a string
strW=str(binarykey)
strL=str(binaryL)
print(strW)
print(strL)
#print()
yourNumber=int(strW,2)
yourKey=int(strL,2)
print(yourNumber)
print(yourKey)
number2letter=chr(yourNumber)
key2letter=chr(yourKey)
print(number2letter)
print(key2letter)
