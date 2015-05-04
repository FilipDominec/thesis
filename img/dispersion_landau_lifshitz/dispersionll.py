#!/usr/bin/env python
#-*- coding: utf-8 -*-

## Import common moduli
import matplotlib, sys, os, time
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import c, hbar, pi

## User settings
epsll_contours          = 0
epsll_dispersion        = 0
classical_dispersion    = 1
eampli, eomega0, egamma = .0, .35, .001
mampli, momega0, mgamma = .0, .40, .001
outname = "dispersion_vacuum.pdf"

#epsll_contours          = 0
#epsll_dispersion        = 0
#classical_dispersion    = 1
#eampli, eomega0, egamma = .3, .35, .001
#mampli, momega0, mgamma = .0, .40, .001
#outname = "dispersion_simple_el.pdf"
#
#epsll_contours          = 1
#epsll_dispersion        = 1
#classical_dispersion    = 1
#eampli, eomega0, egamma = .3, .35, .001
#mampli, momega0, mgamma = .0, .40, .001
#outname = "dispersion_ll_el.pdf"
#
#epsll_contours          = 1
#epsll_dispersion        = 1
#classical_dispersion    = 1
#eampli, eomega0, egamma = .0, .35, .001
#mampli, momega0, mgamma = .1, .40, .001
#outname = "dispersion_ll_mag.pdf"

#epsll_contours          = 1
#epsll_dispersion        = 1
#classical_dispersion    = 1
#eampli, eomega0, egamma = .3, .35, .001
#mampli, momega0, mgamma = .1, .40, .001
#outname = "dispersion_ll_elmag.pdf"

#


## Use LaTeX
matplotlib.rc('text', usetex=True)
matplotlib.rc('font', size=12)
matplotlib.rc('text.latex', preamble = '\usepackage{amsmath}, \usepackage{yfonts}, \usepackage{txfonts}, \usepackage{lmodern},')
plt.figure(figsize=(12,6))

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
    epsll = eps_clas*np.ones_like(ks)   +   (1-1/mu_clas) * k**2 / omegas**2             ## FIXME generate data for the points on grid
    dispcontour = epsll * omegas**2 / k**2

    epslls.append(epsll)
    dispcontours.append(dispcontour)
epslls = np.array(epslls).T
dispcontours = np.array(dispcontours).T


## Plot contours for L-L permittivity
plt.subplot(1, 2, 2) ## ensure the plot region is a square
#extent = max(-np.min(epslls), np.max(epslls))
extent = 30
if epsll_contours:
    contours = plt.contourf(ks, omegas, np.real(epslls), levels=np.linspace(-extent,extent,50), cmap=matplotlib.cm.RdBu_r, extend='both', alpha=1)
    #contours = plt.contourf(ks, omegas, np.real(dispcontours), levels=np.linspace(-extent,extent,50), cmap=matplotlib.cm.RdBu_r, extend='both', alpha=1)
    for contour in contours.collections: contour.set_antialiased(False)     ## optional: avoid white aliasing (for matplotlib 1.0.1 and older) 
    plt.colorbar().set_ticks(np.arange(-extent, extent+1, 5))                        ## optional: colorbar
if epsll_dispersion:
    plt.contour(ks, omegas, np.real(dispcontours), levels=[1,1], colors='k')      ## optional: plot black contour at zero

## Plot the shape of permittivity and permeability
plt.subplot(1, 2, 1)
plt.plot(eps_clas, omegas, lw=2, c='m', label="$\\varepsilon_r'(\\omega)$")
plt.plot(mu_clas,  omegas, lw=2, c='y', label="$\\mu_r'(\\omega)$")
plt.ylim((-0.,1.)); plt.yscale('linear')
plt.xlim((-5.,10.)); plt.xscale('linear')
plt.xlabel(u"relative permittivity $\\varepsilon_r$ and permeability $\\mu_r$"); 
plt.ylabel(u"frequency $\\omega$"); 
plt.grid(); plt.legend()

## Plot classical dispersion contours
plt.subplot(1, 2, 2)
if classical_dispersion:
    plt.plot(omegas*np.sqrt(eps_clas * mu_clas), omegas, lw=2, c='g', alpha=.5)

plt.ylim((-0.,1.)); plt.yscale('linear')
plt.xlim((-0.,1.)); plt.xscale('linear')

## ==== Outputting ====
## Finish the plot + save 
plt.xlabel(u"wavenumber $k$"); 
plt.ylabel(u"frequency $\\omega$"); 
plt.grid()
plt.legend(prop={'size':10}, loc='upper right')
plt.savefig(outname, bbox_inches='tight')

