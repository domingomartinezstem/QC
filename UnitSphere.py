# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 12:11:28 2019

@author: domin
"""

import numpy as np


from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

phi = np.linspace(0, np.pi, 20)
theta = np.linspace(0, 2 * np.pi, 30)
x = np.outer(np.sin(theta), np.cos(phi))
y = np.outer(np.sin(theta), np.sin(phi))
z = np.outer(np.cos(theta), np.ones_like(phi))
H=(1/np.sqrt(2))*np.array([[1, 1],[1, -1]])


angle1=30
angle2=0
theta1=angle1*np.pi/180
phi1=angle2*np.pi/180
xi=np.sin(theta1)*np.cos(phi1)
yi=np.sin(theta1)*np.sin(phi1)
zi=np.cos(theta1)
psi=np.real(np.array([[np.cos(theta1/2)],[np.exp(1j*phi1)*np.sin(theta1/2)]]))
print(angle1, angle2)
print(xi,yi,zi)

psi2=np.matmul(H,psi)
#solve for theta2
theta2=2*np.arccos(psi2[0,0])
phi2=np.real(np.log(psi2[1,0]/np.sin(theta2/2))/1j)
#get new x,y,z
xi2=np.sin(theta2)*np.cos(phi2)
yi2=np.sin(theta2)*np.sin(phi2)
zi2=np.cos(theta2)
print(xi2,yi2,zi2)
fig=plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, projection='3d', aspect='equal')
origin = [[0],[0],[0]]
ax.quiver(*origin, [xi],[yi],[zi],arrow_length_ratio=0.1)
ax.quiver(*origin, [xi2],[yi2],[zi2],arrow_length_ratio=0.1)

ax.quiver([-1],[0],[0], [2],[0],[0], color='k', lw=1.5,arrow_length_ratio=0)
ax.quiver([0],[-1],[0], [0],[2],[0], color='k', lw=1.5,arrow_length_ratio=0)
ax.quiver([0],[0],[-1], [0],[0],[2], color='k', lw=1.5,arrow_length_ratio=0)

ax.plot_wireframe(x, y, z, color='y', rstride=1, cstride=1)
ax.scatter(xi, yi, zi, s=100, c='r', zorder=10)
ax.scatter(xi2, yi2, zi2, s=100, c='r', zorder=10)

ax.view_init(azim=20, elev=10) 