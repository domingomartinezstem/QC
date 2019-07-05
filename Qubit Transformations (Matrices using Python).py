# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:52:19 2019

@author: domin
"""
import numpy as np
from numpy.linalg import inv

#Assignment: Hermitian Matrices using Python
def twobytwo(a, b, c, d):
    #MatrixInv= (1/(a*d - c*b))*np.array([[a, -b],[-c, d]])
    Matrix = np.matrix([[a, b],[c, d]])
    Herm=Matrix.getH()
    Sym = np.array([[a, c],[b,d]])
 
    if Matrix[0,0] == Herm[0,0] and Matrix[0,1] == Herm[0,1]:
        e=1;
    else: 
        e=0;
    if Matrix[1,0] == Herm[1,0] and Matrix[1,1] == Herm[1,1]:
        f=1;
    else:
        f=0;
    if e==1 and f ==1:
        print("Herm")
        #print ("isa Hermitian")
    if Matrix[0,0] == Sym[0,0] and Matrix[0,1] == Sym[0,1]:
        g=1;
    else: 
        g=0;
    if Matrix[1,0] == Sym[1,0] and Matrix[1,1] == Sym[1,1]:
        h=1;
    else:
        h=0;
    if g ==1 & h ==1:
        print("sym")
    #if Sym == Matrix: 
        #print("isa Symmetric")
    return Matrix
print()

#Assignment: Unitary Matrices using Python

def twobytwo2(a, b, c, d):
    #MatrixInv= (1/(a*d - c*b))*np.array([[a, -b],[-c, d]])
    Matrix2 = np.matrix([[a, b],[c, d]])
    MatR= Matrix2.round(decimals=6)
    Inv = inv(Matrix2)
    InvR = Inv.round(decimals=6)
    Trans=np.matrix([[a,c],[b,d]])
    TransR= Trans.round(decimals=6)
    Uni= Matrix2.getH()
    UniR=Uni.round(decimals=6)
    
    print(MatR)
    print()
    print(InvR)
    print()
    print(TransR)
    print()
    print(UniR)
 #involution Matrix2=Inv 
    if MatR[0,0] == InvR[0,0] and MatR[0,1] == InvR[0,1]:
        e=1;
    else: 
        e=0;
    if MatR[1,0] == InvR[1,0] and MatR[1,1] == InvR[1,1]:
        f=1;
    else:
        f=0;
    if e==1 and f ==1:
        print("Involution")
        #print ("isa Hermitian")
    if TransR[0,0] == InvR[0,0] and TransR[0,1] == InvR[0,1]:
        g=1;
    else: 
        g=0;
    if TransR[1,0] == InvR[1,0] and TransR[1,1] == InvR[1,1]:
        h=1;
    else:
        h=0;
    if g ==1 & h ==1:
        print("Orthogonal")
    if UniR[0,0] == InvR[0,0] and UniR[0,1] == InvR[0,1]:
        i=1;
    else: 
        i=0;
    if UniR[1,0] == InvR[1,0] and UniR[1,1] == InvR[1,1]:
        j=1;
    else:
        j=0;
    if i ==1 & j ==1:
        print("Unitary")
    #if Sym == Matrix: 
        #print("isa Symmetric")
    return MatR

Y1=twobytwo2(0,-1j, 1j,0)
print()
S1=twobytwo2(1,0,0,1j)
print()
x1=1/np.sqrt(2)
H1=twobytwo2(x1, x1, x1, -x1)
print()
Q1=twobytwo2(x1, x1, 1j*x1, -1j*x1)
print()


#Assignment: Rotation Matrices using Python

angle=45
theta=angle*(np.pi/180)
#Rot=np.matrix([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
R1=twobytwo2(np.cos(theta), -np.sin(theta), np.sin(theta), np.cos(theta))

V_ket = np.array([[0],[1]])
H_ket = np.array([[1],[0]])
H_ket2 = np.matmul(R1,H_ket)
V_ket2 = np.matmul(R1,V_ket)
print(H_ket)
import matplotlib.pyplot as plt
originx=0
originy=0
V_polar = np.array([[originx, originy, V_ket[0,0], V_ket[1,0]]])
H_polar = np.array([[originx, originy, H_ket[0,0], H_ket[1,0]]])
V_polar2 = np.array([[originx, originy, V_ket2[0,0], V_ket2[1,0]]])
H_polar2 = np.array([[originx, originy, H_ket2[0,0], H_ket2[1,0]]])

X, Y, U, V = zip(*V_polar)
X1, Y1, U1, V1 = zip(*H_polar)
X2, Y2, U2, V2 = zip(*V_polar2)
X3, Y3, U3, V3 = zip(*H_polar2)

plt.figure(figsize=(5,5))
ax = plt.gca()
ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color='k')
ax.quiver(X1, Y1, U1, V1, angles='xy', scale_units='xy', scale=1, color='k')
ax.quiver(X2, Y2, U2, V2, angles='xy', scale_units='xy', scale=1, color='r')
ax.quiver(X3, Y3, U3, V3, angles='xy', scale_units='xy', scale=1, color='r')

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])

plt.draw()
plt.show()



