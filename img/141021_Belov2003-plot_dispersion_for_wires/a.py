#!/usr/bin/env python
#-*- coding: utf-8 -*-

## Import common moduli
import matplotlib, sys, os, time
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import c, hbar, pi

## Use LaTeX
matplotlib.rc('text', usetex=True)
matplotlib.rc('font', size=8)
matplotlib.rc('text.latex', preamble = '\usepackage{amsmath}, \usepackage{yfonts}, \usepackage{txfonts}, \usepackage{lmodern},')

eps0 = 1
c = 1
qrho = np.linspace(-10,10,1000)
omegas = np.linspace(0.1, 2, 10)
#omegas = [1,3,10]
for omega, color in zip(omegas, matplotlib.cm.hsv(np.linspace(0,1,len(omegas)))): 
    epsz = eps0 - (1./omega)**2
    qz = np.sqrt(omega**2/c**2 - eps0/epsz * qrho**2)
    plt.plot(qrho, qz, c=color)


## Simple axes
#plt.ylim((-0.1,1.1)); plt.yscale('linear')
#plt.xlim((-0.1,1.1)); plt.xscale('linear')

## ==== Outputting ====
## Finish the plot + save 
plt.xlabel(u"x"); 
plt.ylabel(u"y"); 
plt.grid()
plt.legend(prop={'size':10}, loc='upper right')
plt.savefig("output.png", bbox_inches='tight')

