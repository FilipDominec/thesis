#!/usr/bin/env python
#-*- coding: utf-8 -*-

## Import common moduli
import matplotlib, sys, os, time
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import c, hbar, pi

## Use LaTeX
matplotlib.rc('text', usetex=True)
matplotlib.rc('font', size=12)
matplotlib.rc('text.latex', preamble = '\usepackage{amsmath}, \usepackage{yfonts}, \usepackage{txfonts}, \usepackage{lmodern},')

## Generate gridded data from a given 2D function (TODO)
plt.subplot(1, 1, 1, adjustable='box', aspect=1.0) ## ensure the plot region is a square
ks = np.linspace(0, 1, 400)
omegas = np.linspace(0, 1, 400)
zs = []
def lorentz(omega, sigma, omega0, gamma):
    return 1 + sigma/(omega0**2-omega**2 + 1j*gamma**2) ## FIXME

for omega in omegas:
    eps_clas = lorentz(omega, sigma=.2, omega0=.35, gamma=.001) * np.ones_like(ks)
    mu_clas  = lorentz(omega, sigma=.1, omega0=.40, gamma=.001)


    # the correct equation?
    z = (eps_clas + ks**2 *(1-1/mu_clas) )/ks**2 * omega**2             ## generate data for the points on grid

    # this leads to copy the unphysical k = (eps*mu)**1 curve!
    #z = (eps_clas + ks**1/omega*(1-1/mu_clas) )/ks**2*omega**2             ## generate data for the points on grid

    # debug with no magnetic resonance:
    #z = (eps_clas                             )/ks**2 * omega**2             ## generate data for the points on grid

    #z = (eps_clas                       )**.5/ks*y             ## generate data for the points on grid
    zs.append(z)
zs = np.array(zs)



## Plot contours for gridded data
#extent = max(-np.min(zs), np.max(zs))
extent = 20
contours = plt.contourf(ks, omegas, np.real(zs), levels=np.linspace(-extent,extent,50), cmap=matplotlib.cm.RdBu_r, extend='both')
for contour in contours.collections: contour.set_antialiased(False)     ## optional: avoid white aliasing (for matplotlib 1.0.1 and older) 
plt.colorbar() #.set_ticks([-1, -.25, 0, .25, 1])                        ## optional: colorbar
plt.clabel(plt.contour(ks, omegas, np.real(zs), levels=[1,1], colors='k'))      ## optional: plot black contour at zero

eps_clas = lorentz(omegas, sigma=.2, omega0=.35, gamma=.001) * np.ones_like(ks)
mu_clas  = lorentz(omegas, sigma=.1, omega0=.40, gamma=.001)
#exponents = np.linspace(.5, 1, 6)
exponents = [.5]
for exponent, color in zip(exponents, matplotlib.cm.hsv(np.linspace(0,1,len(exponents)))): 
    plt.plot(omegas*(eps_clas * mu_clas**1)**exponent, omegas, lw=.5, c=color)

plt.ylim((-0.,1.)); plt.yscale('linear')
plt.xlim((-0.,1.)); plt.xscale('linear')

## ==== Outputting ====
## Finish the plot + save 
plt.xlabel(u"wave vector $k$"); 
plt.ylabel(u"frequency $\\omega$"); 
plt.grid()
plt.legend(prop={'size':10}, loc='upper right')
plt.savefig("output2.png", bbox_inches='tight')

