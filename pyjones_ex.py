# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:01:57 2019

@author: domin
"""
#you need to install pyjones first from the anaconda command prompt
#pip install pyjones


from py_pol import degrees, np
from py_pol.jones_vector import Jones_vector
from py_pol.drawings import draw_ellipses_jones
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from py_pol import degrees, np
from py_pol.stokes import Stokes
from py_pol.mueller import Mueller
from py_pol.drawings import draw_poincare_sphere, draw_on_poincare


j0=Jones_vector('j0')
j0.elliptical_light(a=1, b=2, phase=45*degrees, angle=45*degrees)
ax,fig=j0.draw_ellipse()
plt.savefig('ellipse_Jones_1.png')

#definition of a list Jones vectors

Jones_vectors_0=[]

j0=Jones_vector('j0')
j0.linear_light(amplitude=1, angle=0*degrees)


angles = np.linspace(0, 180*degrees, 6, endpoint=False)

for i, angle in enumerate(angles):
    ji=j0.rotate(angle=angle, keep=True)
    Jones_vectors_0.append(ji)
    print(ji)

print (Jones_vectors_0)

ax,fig = draw_ellipses_jones(Jones_vectors_0, filename='ellipse_Jones_2.png')


Stokes_points2 = []

s2 = Stokes('s2')
s2.linear_light(angle=45*degrees, intensity=1)
print(s2)

M1 = Mueller('M1_retarder')
M1.quarter_wave()

#M1.quarter_waveplate(angle=0 * degrees)
print(M1)

angles = np.linspace(0, 180 * degrees, 90)

for i, angle in enumerate(angles):
    M_rot=M1.rotate(angle=angle, keep=True)
    s_rot = M_rot*s2
    Stokes_points2.append(s_rot)
    
ax, fig=draw_poincare_sphere(stokes_points=Stokes_points2 , kind='line', color='b',
                             label='rotating quarter wave', filename='poincare3.png')

plt.legend();