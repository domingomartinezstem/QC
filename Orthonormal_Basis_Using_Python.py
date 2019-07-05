# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:36:08 2019

@author: domin
"""


from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import random

class basisState:
    
    def unitvec():
        u1=random.random()
        u1a=u1*u1
        u2=np.sqrt(1-u1a)
        return u1, u2
    u1,u2=unitvec()
    S1=u1*u1
    S2=u2*u2

    q1,q2 =unitvec()
#print(u1,u2)
#print(S1+S2)
#print()

    def basisvec(u1,u2):
        x1=1/np.sqrt(np.square(-u1/u2) +1)
        x2=-(u1/u2)*x1
        return x1, x2

    x1,x2=basisvec(u1,u2)
    R1=x1*x1
    R2=x2*x2
#print(x1,x2)
#print(R1+R2)



    originx=0
    originy=0

    basis1 = np.array([[originx, originy, u1, u2]])
    basis2 = np.array([[originx, originy, x1, x2]])
    Qubit1 = np.array([[originx, originy, q1, q2]])


    X, Y, U, V = zip(*basis1)
    X2, Y2, U2, V2 = zip(*basis2)
    X3, Y3, U3, V3 = zip(*Qubit1)

    plt.figure(figsize=(10,10))
    ax = plt.gca()
    ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color='k')
    ax.quiver(X2, Y2, U2, V2, angles='xy', scale_units='xy', scale=1, color='k')
    ax.quiver(X3, Y3, U3, V3, angles='xy', scale_units='xy', scale=1, color='r')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])

    plt.draw()
    plt.show()

