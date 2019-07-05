# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:41:05 2018

@author: domin
"""
#this works!
def encrypt(sentence):
    result = []
    for letter in sentence:
        l= ord(letter)
        result.append(l)
    print("encrypted message")
    for numbers in result:
        print(numbers, end='')
        print("", end='')
    print()
    decrypt(result)
    
def decrypt(result):
    end_string=""
    for numbers in result:
        l=int(numbers)
        l=l
        l=chr(l)
        end_string=end_string + l
    print("Your decrypted message")
    print(end_string)
def main():
    s=input("input a sentence for encryption:  ")
    encrypt(s)

if __name__=='__main__':
    main()