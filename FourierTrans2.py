# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:04:29 2019

@author: domin
"""

import matplotlib.pyplot as plt
from numpy import linalg as LA
import numpy as np
from scipy import fftpack

#f=8,4,2,1 for each additional qubit
f = 2  # Frequency, in cycles per second, or Hertz
f_s = 40  # Sampling rate, or number of measurements per second

t = np.linspace(0, 1, f_s, endpoint=False)
x0=np.exp(1j*2*np.pi*f*t)/2;
x1=np.exp(1j*2*np.pi*f*t)/2;

#changing the negative sign changes the frequency 

H=(1/np.sqrt(2))*np.array([[1, 1],[1, -1]])

def Arraymul(A,x):
    xt1=A[0,0]*np.real(x)+A[0,1]*np.imag(x)
    xt2=A[1,0]*np.real(x)+A[1,1]*np.imag(x)
    XS = xt1+xt2
    return XS,xt1,xt2
#gate applied to qubit0 only
XS,xt1,xt2 = Arraymul(H,x0)
#add both states
Xq=XS+x1
fig, ax = plt.subplots()
ax.plot(t, np.real(Xq),t,np.imag(Xq))
ax.set_xlabel('Time [s]')
ax.set_ylabel('Signal amplitude');

Xff = fftpack.fft(Xq) 
freqs = fftpack.fftfreq(len(Xq)) *f_s
#freqs = np.fft.fftshift(freqs)

fig, ax = plt.subplots()
ax.stem(freqs, np.abs(Xff)/f_s)
#ax.stem(freqs/f_s, np.abs(np.imag(X1))/f_s)

ax.set_xlabel('Frequency in Hertz [Hz]')
ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
ax.set_xlim(-3.25 , 3.25 )
ax.set_ylim(-1.25, 1.25)