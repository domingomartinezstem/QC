# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:12:41 2019

@author: domin
"""
#import Orthonormal_Basis_Using_Python
import numpy as np
import random
#qH,qV =unitvec()

input_basis=input("type a number to prepare a qubit: 1=H/V 2:D/A 3:RC/LC  ")
Hor=np.array([[1],[0]])
Ver=np.array([[0],[1]])

Q=(1/np.sqrt(2))*np.array([[1, 1],[1j, -1j]])
Qdag=(1/np.sqrt(2))*np.array([[1, -1j],[1, 1j]])
H=(1/np.sqrt(2))*np.array([[1, 1],[1, -1]])
I=np.array([[1, 0],[0, 1]])
X=np.array([[0, 1],[1, 0]])
Y=np.array([[0, -1j],[1j, 0]])
Z=np.array([[1, 0],[0,-1]])
L=[Q,H,I,X,Y,Z]
Lable=['Qdag','H','I','X','Ydag','Z']


if input_basis == '3':
    print("prepare in RC/LC basis")
    U1=(1/np.sqrt(2))*np.array([[1],[1j]])
    U2=(1/np.sqrt(2))*np.array([[1],[-1j]])

if input_basis == '2':
    print("prepare in D/A basis")
    U1=(1/np.sqrt(2))*np.array([[1],[1]])
    U2=(1/np.sqrt(2))*np.array([[1],[-1]])
if input_basis == '1':
    print("prepare in H/V basis")
    U1=Hor
    U2=Ver
print('basis 1: ', U1)
print('basis 2: ' , U2)
print()
  

for i in range(6):
    F1=np.matmul(L[i],Hor)
    #Q*H=U1 (if U1=right circular), the Qdag*U1=H 
    if F1[0,0] == U1[0,0] and F1[1,0]==U1[1,0]:
        print('The unitary matrix is: ' + Lable[i])
        #prints the complex conjuagte transpose 
print()
def unitvec():
    u1=random.random()
    u1a=u1*u1
    u2=np.sqrt(1-u1a)
    return u1, u2

qH, qV = unitvec()
Qstate1=np.array([[qH],[qV]])

print('Qubit state Horizontal:',qH)
print('Qubit state Vertical:', qV)
U1t=np.transpose(U1)
U2t=np.transpose(U2)
prob1=np.square(np.dot(U1t,Qstate1))
prob2=np.square(np.dot(U2t,Qstate1))

print('probability of measuring in basis 1: ', prob1[0])
print('probability of measuring in basis 2: ', prob2[0])

        