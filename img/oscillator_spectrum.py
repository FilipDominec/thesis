#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
This is a manual computation of Fourier transform, to verify that the numpy.fft's or scipy's built-in Fast Fourier Transform
behaves as expected also in terms of accumulated power etc.

The curves obtained using the 
    1) frequency `f'
    2) angular frequency `omega'
are obviously different: when the _angular_ frequency `omega' is used, its axis dilates by 2pi, and 
accordingly, the values have to be divided by sqrt(2pi) (NB this is due to the Fourier-Plancherel theorem, 
which is tested below)

The frequency `f' approach is used by numpy.fft, and by uncommenting its section it can be shown that
it gives nearly identical data to the manually computed FT.

Public domain, 2014 F. Dominec
"""

## Import common moduli
import matplotlib, sys, os, time
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import c, hbar, pi

## Use LaTeX
matplotlib.rc('text', usetex=True)
matplotlib.rc('font', size=12)
matplotlib.rc('text.latex', preamble = '\usepackage{amsmath}, \usepackage{yfonts}, \usepackage{txfonts}, \usepackage{lmodern},')
#matplotlib.rc('font',**{'family':'serif','serif':['Computer Modern Roman, Times']})  ## select fonts
plt.figure(figsize=(10,4))
plt.subplot(121)

## Generate time-domain data
x = np.linspace(-3, 25, 3000)
y = (np.sign(x)/2+.5) * np.sin(x*2*pi)*2*pi * np.exp(-x/2)  ## damped oscillator
#(note: Plancherel theorem is not valid for delta function in numerical computation)
y[int(len(x)*(-x[0]/(x[-1]-x[0])))] +=         1 / (x[1]-x[0])  ## delta function suitable for f-convention 
#y = (np.sign(x+.5)/2+.5) * (np.sign(.5-x)/2+.5)        ## square impulse
plt.plot(x,y, c='#aa0088', label="Real part")
plt.grid()
plt.ylim((-10,10)); plt.yscale('linear')

## Plot time-domain 
plt.xlabel(u"time $t$") 
plt.ylabel(u"medium response $\\chi_e(t) + \\delta(t)$") 
plt.title(u"\\textbf{a)} Time domain")
#plt.title('Right Title', loc='right')


## Scipy's  implementation of Fast Fourier transform
plt.subplot(122)
freq    = np.fft.fftfreq(len(x), d=(x[1]-x[0]))         # calculate the frequency axis with proper spacing
yf2     = np.fft.fft(y, axis=0) / len(x) * 2*np.pi      # calculate the FFT values
freq    = np.fft.fftshift(freq)                         # ensures the frequency axis is a growing function
yf2     = np.fft.fftshift(yf2) / np.exp(1j*2*np.pi*freq * x[0])   # dtto, and corrects the phase for the case when x[0] != 0
truncated = np.logical_and(freq>0, freq<np.inf)         # (optional) get the frequency range
(yf2, freq) = map(lambda x: x[truncated], (yf2, freq))    # (optional) truncate the data points

#    ## Own implementation of slow Fourier transform - in f
#    f = np.linspace(-5, 5, 1000)
#    yf = np.sum(y * np.exp(-1j*2*np.pi*np.outer(f,x)), axis=1) * (x[1]-x[0])
#    plt.plot(f, np.real(yf), c='g', label='FT in $f$-convention')
#    plt.plot(f, np.imag(yf), ls='--', c='g')

#   ## Test the Kramers-Kronig relations - in f
#   def naive_hilbert_transform(x, y, new_x):
#       old_x_grid, new_x_grid = np.meshgrid(x, new_x)
#       return -1j * np.sum(y * np.arctan(1/(new_x_grid - old_x_grid)/200)*200, axis=1) / len(x) * 2*np.pi
#   new_f = np.linspace(0, 5, 100)
#   conv = naive_hilbert_transform(f, yf, new_f)
#   plt.plot(new_f, conv.real, ls='-', c='k', alpha=1, lw=.5, label='KKR in $f$') 
#   plt.plot(new_f, conv.imag, ls='--', c='k', alpha=1, lw=.5) 


## Own implementation of slow Fourier transform - in omega XXX
omega = np.linspace(-15, 15, 3000)  # (note: if only positive frequencies are used, the energy will be half of that in time-domain)
yomega = np.sum(y * np.exp(-1j*        np.outer(omega,x)), axis=1) * (x[1]-x[0])
plt.plot(omega, np.real(yomega), c='#008844', label='Real part') # , label='FT in $\\omega$-convention'
plt.plot(omega, np.imag(yomega), c='#88aa00', lw=.8, ls='--', label='Imaginary part')
#plt.plot(omega, -np.imag(yomega)/np.real(yomega), c='k', label='tg($\\delta)$')        # tg(delta) is often used in microwave engineering

#   ## Test the Kramers-Kronig relations - in omega
#   new_omega = np.linspace(5, 8, 900)
#td = np.trapz(y=np.abs(y)**2, x=x)
#print 'Energy in timedomain      :', td
#   conv = naive_hilbert_transform(omega, yomega, new_omega)
#   plt.plot(new_omega, conv.real, ls='-', c='k', alpha=1, lw=.5, label='KKR in $\\omega$') 
#   plt.plot(new_omega, conv.imag, ls='--', c='k', alpha=1, lw=.5) 


## Plot
plt.xlim((-0,15)); plt.xscale('linear')
plt.ylim((-10,10)); plt.yscale('linear')
plt.xlabel(u"angular frequency $\\omega$"); 
plt.ylabel(u"local permittivity $\\varepsilon_r(\\omega)$"); 
plt.title(u"\\textbf{b)} Frequency domain")
plt.grid()


## Test the Plancherel theorem - the energies in time-domain and frequency domain should equal
#td = np.trapz(y=np.abs(y)**2, x=x)
#print 'Energy in timedomain      :', td
#fd = np.trapz(y=np.abs(yf)**2, x=f) 
#print 'Energy in freqdomain f    :', fd, ', ratio:',    fd/td
#fdomega = np.trapz(y=np.abs(yomega)**2, x=omega) 
#print 'Energy in freqdomain omega:', fdomega, ', ratio:',    fdomega/td


## ==== Outputting ====
## Finish the plot + save 
plt.legend(prop={'size':10}, loc='upper right')
plt.savefig("oscillator_spectrum.pdf", bbox_inches='tight')

