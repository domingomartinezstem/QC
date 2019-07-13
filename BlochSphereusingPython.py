# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 13:40:52 2019

@author: domin
"""
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

#used to plot the Bloch sphere
phi = np.linspace(0, np.pi, 20)
theta = np.linspace(0, 2 * np.pi, 30)
blochX = np.outer(np.sin(theta), np.cos(phi))
blochY = np.outer(np.sin(theta), np.sin(phi))
blochZ = np.outer(np.cos(theta), np.ones_like(phi))

#point on the Bloch sphere
theta1=np.pi/4
phi1=0
x=np.sin(theta1)*np.cos(phi1)
y=np.sin(theta1)*np.sin(phi1)
z=np.cos(theta1)
print(x,y,z)
X=np.array([[0,1],[1,0]])
psi=np.array([[np.cos(theta1/2)],[np.sin(theta1/2)]])
psi2=np.matmul(X,psi)

theta2=np.arccos(psi2[0,0])*2
x2=np.sin(theta2)*np.cos(0)
y2=np.sin(theta2)*np.sin(0)
z2=np.cos(theta2)


fig=plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, projection='3d', aspect='equal')

#connect a vector to the point on the sphere
origin = [[0],[0],[0]]
ax.quiver(*origin, [x],[y],[z],arrow_length_ratio=0.1)
ax.quiver(*origin, [x2],[y2],[z2],color='r',arrow_length_ratio=0.1)


#generates the X,Y,Z axis on the Bloch sphere
ax.quiver([-1],[0],[0], [2],[0],[0], color='k', lw=1.5,arrow_length_ratio=0)
ax.quiver([0],[-1],[0], [0],[2],[0], color='k', lw=1.5,arrow_length_ratio=0)
ax.quiver([0],[0],[-1], [0],[0],[2], color='k', lw=1.5,arrow_length_ratio=0)
#plots the sphere
ax.plot_wireframe(blochX,blochY,blochZ, color='y', rstride=1, cstride=1)
#plots the point
ax.scatter(x, y, z, s=100, c='r', zorder=10)
ax.scatter(x2, y2, z2, s=100, c='r', zorder=10)

#changes the values below to angle of orientation
ax.view_init(azim=20, elev=10) 