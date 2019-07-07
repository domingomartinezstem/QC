# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 11:57:16 2019

@author: domin
"""
import matplotlib.pyplot as plt
from numpy import linalg as LA
import numpy as np
import random



#Generate 1st eigenvector (basis)
def unitvec():
    u1=random.random()
    u1a=u1*u1
    u2=np.sqrt(1-u1a)
    return u1, u2
u1,u2=unitvec()
U1 = np.array([[u1],[u2]]) 
#Generate the 2nd eigenvector 
def basisvec(u1,u2):
    x1=1/np.sqrt(np.square(-u1/u2) +1)
    x2=-(u1/u2)*x1
    return x1, x2
x1,x2=basisvec(u1,u2)
U2 = np.array([[x1],[x2]])
UnitaryM=np.matrix([[u1, x1],[u2, x2]])
UnitMdag=UnitaryM.getH()  #to verify UnitaryM is Hermetian

eigval, eigvec = LA.eig(UnitaryM)
print(eigval)
print(eigvec)
print()
print(U1)
print(U2)
print()

#generate random qubit state 
q1, q2 = unitvec()
Qstate = np.array([[q1],[q2]])
U1t=np.transpose(eigvec[:,0])
U2t=np.transpose(eigvec[:,1])
prob1=np.square(np.dot(U1t,Qstate))
prob2=np.square(np.dot(U2t,Qstate))
print('probability of obtaining outcome of eigenvalue 1: ', prob1[0])
print('probability of obtaining outcome of eigenvalue -1:  ', prob2[0])
#expectation value using both methods 
Expect= np.transpose(Qstate)*np.matmul(UnitaryM,Qstate)
Expect2= eigval[0]*prob1[0] + eigval[1]*prob2[0]
print('Expectation value: ',Expect)
#print(Expect2)



originx=0
originy=0

basis1 = np.array([[originx, originy, u1, u2]])
basis2 = np.array([[originx, originy, x1, x2]])
eigenvec1= np.array([[originx,originy,eigvec[0,0],eigvec[1,0]]])
eigenvec2= np.array([[originx,originy,eigvec[0,1],eigvec[1,1]]])

Qubit1 = np.array([[originx, originy, q1, q2]])


X, Y, U, V = zip(*basis1)
X2, Y2, U2, V2 = zip(*basis2)
X3, Y3, U3, V3 = zip(*Qubit1)
X4, Y4, U4, V4 = zip(*eigenvec1)
X5, Y5, U5, V5 = zip(*eigenvec2)
plt.figure(figsize=(15,15))
ax = plt.gca()
ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color='k')
ax.quiver(X2, Y2, U2, V2, angles='xy', scale_units='xy', scale=1, color='k')
ax.quiver(X3, Y3, U3, V3, angles='xy', scale_units='xy', scale=1, color='r')
ax.quiver(X4, Y4, U4, V4, angles='xy', scale_units='xy', scale=1, color='g')
ax.quiver(X5, Y5, U5, V5, angles='xy', scale_units='xy', scale=1, color='g')

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])


plt.draw()
plt.show()






##code below is just testing
#n=1/np.sqrt(2)
#p=np.exp(1j*np.pi/4)
##pa1=np.sqrt(8)*np.exp(-1j*np.pi/3)
##pa2=np.sqrt(8)*np.exp(1j*np.pi/3)
#X=np.matrix([[0, 1],[1, 0]])
#T=np.matrix([[1, 0],[0, p]])
#Tdag=T.getH()
##A=(1/3)*np.array([[1, pa1],[pa2, -1]])
#TX=np.sqrt(2)*np.matmul(T,X)
#A1=np.matmul(TX,Tdag)
##phi1=(1/np.sqrt(2))*np.matrix([[pow(2,.5)],[np.exp(1j*np.pi/4)]])
##phi2=(1/np.sqrt(2))*np.matrix([[1],[-pow(2,.5)*np.exp(1j*np.pi/4)]])
##phi1=np.matrix([[np.cos(np.pi/6)],[p*np.sin(np.pi/6)]])
##phi2=np.matrix([[-np.sin(np.pi/6)],[p*np.cos(np.pi/6)]])
##psi=np.matrix([[n],[n*p]])
##UU=np.matrix([[phi1[0,0], phi2[0,0]],[phi1[1,0], phi2[1,0]]])
#uw, uv = LA.eig(A1)
##
#print(uw)
#print(uv)
#phi1=uv[:,0]
#phi2=uv[:,1]
##print()
#R=n*np.array([[1],[1j]])
#phi1t=phi1.getH()
#phi2t=phi2.getH()
#prob1s=np.square(np.dot(phi1t,R))
#prob2s=np.square(np.dot(phi2t,R))
#print('probability of phi1: ', prob1s[0])
#print('probability of phi2:  ', prob2s[0])
##


