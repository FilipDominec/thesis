#!/usr/bin/env python
#-*- coding: utf-8 -*-

## Import common moduli
import matplotlib, sys, os, time
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import c, hbar, pi


eampli, eomega0, egamma = .2, .35, .001
mampli, momega0, mgamma = .0, .40, .001

## Use LaTeX
matplotlib.rc('text', usetex=True)
matplotlib.rc('font', size=12)
matplotlib.rc('text.latex', preamble = '\usepackage{amsmath}, \usepackage{yfonts}, \usepackage{txfonts}, \usepackage{lmodern},')
plt.figure(figsize=(16,8))

## An exact curve for the analytic solution of a damped oscillator
def lorentz(omega, omega0, gamma, ampli):
    return ampli / (omega0**2 - omega**2 + 1j*omega*gamma) 

## Generate gridded data from a given 2D function (TODO)
ks = np.linspace(0, 1, 400)
omegas = np.linspace(0, 1, 400)

## Generate classical local permittivity and permeability (the same for all wavevectors k)
eps_clas = 1+lorentz(omegas, ampli=eampli, omega0=eomega0, gamma=egamma)
mu_clas  = 1+lorentz(omegas, ampli=mampli, omega0=momega0, gamma=mgamma)

epslls = []
dispcontours = []
for k in ks:
    # Conversion to the Landau-Lifshitz permittivity (mu_ll will be identical to 1, then)
    epsll = (eps_clas*np.ones_like(ks) + k**2 *(1-1/mu_clas))*omegas**2             ## FIXME generate data for the points on grid
    dispcontour = epsll * omegas**0 / k**2

    # this leads to copy the unphysical k = (eps*mu)**1 curve!
    #z = (eps_clas + ks**1/omega*(1-1/mu_clas) )/ks**2*omega**2             ## generate data for the points on grid
    # debug with no magnetic resonance:
    #z = (eps_clas                             )/ks**2 * omega**2             ## generate data for the points on grid
    #z = (eps_clas                       )**.5/ks*y             ## generate data for the points on grid
    epslls.append(epsll)
    dispcontours.append(dispcontour)
epslls = np.array(epslls).T
dispcontours = np.array(dispcontours).T


## Plot contours for L-L permittivity
plt.subplot(1, 2, 2) ## ensure the plot region is a square
#extent = max(-np.min(epslls), np.max(epslls))
extent = 1
contours = plt.contourf(ks, omegas, np.real(dispcontours), levels=np.linspace(-extent,extent,50), cmap=matplotlib.cm.RdBu_r, extend='both', alpha=.3)
for contour in contours.collections: contour.set_antialiased(False)     ## optional: avoid white aliasing (for matplotlib 1.0.1 and older) 
plt.colorbar() #.set_ticks([-1, -.25, 0, .25, 1])                        ## optional: colorbar
plt.clabel(plt.contour(ks, omegas, np.real(dispcontours), levels=[1,1], colors='k'))      ## optional: plot black contour at zero

## Plot classical dispersion contours
plt.subplot(1, 2, 1) ## ensure the plot region is a square
plt.plot(eps_clas, omegas, lw=2, c='m')
plt.plot(mu_clas,  omegas, lw=2, c='y')
#exponents = np.linspace(.5, 1, 6)
exponents = [.5]
plt.subplot(1, 2, 2) ## ensure the plot region is a square
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

