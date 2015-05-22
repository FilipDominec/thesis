#!/usr/bin/env python
#-*- coding: utf-8 -*-

## Import common moduli
import matplotlib, sys, os, time
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import c, hbar, pi

## User settings
#epsll_contours, epsll_dispersion, classical_dispersion    = 0, 0, 1
#eampli, eomega0, egamma = .0, 1., .001
#mampli, momega0, mgamma = .0, 1.2, .001
#outname = "dispersion_vacuum.pdf"
#
#epsll_contours, epsll_dispersion, classical_dispersion    = 0, 0, 1
#eampli, eomega0, egamma = 1., 1., .001
#mampli, momega0, mgamma = .0, 1.2, .001
#outname = "dispersion_simple_el.pdf"
#
#epsll_contours, epsll_dispersion, classical_dispersion    = 1, 1, 1
#eampli, eomega0, egamma = 1., 1., .001
#mampli, momega0, mgamma = .0, 1.2, .001
#outname = "dispersion_ll_el.pdf"
#
#epsll_contours, epsll_dispersion, classical_dispersion    = 1, 1, 1
#eampli, eomega0, egamma = .0, 1., .001
#mampli, momega0, mgamma = .3, 1.2, .001
#outname = "dispersion_ll_mag.pdf"

#epsll_contours, epsll_dispersion, classical_dispersion    = 1, 1, 1
#eampli, eomega0, egamma = 1., 1., .001
#mampli, momega0, mgamma = .3, 1.2, .001
#outname = "dispersion_ll_elmag.pdf"



#epsll_contours, epsll_dispersion, classical_dispersion    = 1, 1, 1
#eampli, eomega0, egamma = 1, 1., .001
#mampli, momega0, mgamma = 0, 1.2, .001
#qampli, qomega0, qgamma = .08, 1., .01
#outname = "dispersion_ll_quadrupp.pdf"
#
#epsll_contours, epsll_dispersion, classical_dispersion    = 1, 1, 1
#eampli, eomega0, egamma = 1, 1., .001
#mampli, momega0, mgamma = 0, 1.2, .001
#qampli, qomega0, qgamma = -.08, 1., .01
#outname = "dispersion_ll_quadrupn.pdf"

epsll_contours, epsll_dispersion, classical_dispersion    = 1, 1, 1
eampli, eomega0, egamma = 1, 1., .001
mampli, momega0, mgamma = 0, 1.2, .001
aampli, aomega0, agamma = -.7, 1., .001
outname = "dispersion_ll_activen.pdf"
#
#epsll_contours, epsll_dispersion, classical_dispersion    = 1, 1, 1
#eampli, eomega0, egamma = 1, 1., .001
#mampli, momega0, mgamma = 0, 1.2, .001
#aampli, aomega0, agamma = .7, 1., .001
#outname = "dispersion_ll_activep.pdf"


## Use LaTeX
matplotlib.rc('text', usetex=True)
matplotlib.rc('font', size=12)
matplotlib.rc('text.latex', preamble = '\usepackage{amsmath}, \usepackage{txfonts}, \usepackage{lmodern},')
plt.figure(figsize=(10,3))

## An exact curve for the analytic solution of a damped oscillator
def lorentz(omega, omega0, gamma, ampli):
    return ampli / (omega0**2 - omega**2 + 1j*omega*gamma) 

## Generate gridded data from a given 2D function (TODO)
ks = np.linspace(0, 3., 400)
omegas = np.linspace(0, 2., 400)

## Generate classical local permittivity and permeability (the same for all wavevectors k)
eps_clas = 1+lorentz(omegas, ampli=eampli, omega0=eomega0, gamma=egamma)
mu_clas  = 1+lorentz(omegas, ampli=mampli, omega0=momega0, gamma=mgamma)
if 'aampli' in locals(): ## account for the optical activity
    activity = lorentz(omegas, ampli=aampli, omega0=aomega0, gamma=agamma)
if 'qampli' in locals(): ## account for the fourth-order expansion terms
    quadrupole = lorentz(omegas, ampli=qampli, omega0=qomega0, gamma=qgamma)


epslls = []
dispcontours = []
for k in ks:
    # Conversion to the Landau-Lifshitz permittivity (mu_ll will be identical to 1, then)
    epsll = eps_clas*np.ones_like(ks)   +   (1-1/mu_clas) * k**2 / omegas**2            ## note that this should divided by mu_0 for realistic values
    if 'aampli' in locals(): ## account for the optical activity
        epsll += activity * k**1
    if 'qampli' in locals(): ## account for the fourth-order expansion terms
        epsll += quadrupole * k**4
    dispcontour = epsll * omegas**2 / k**2

    epslls.append(epsll)
    dispcontours.append(dispcontour)
epslls = np.array(epslls).T
dispcontours = np.array(dispcontours).T


## Plot contours for L-L permittivity
plt.subplot(1, 2, 2) ## ensure the plot region is a square
#extent = max(-np.min(epslls), np.max(epslls))
extent = 20
if epsll_contours:
    contours = plt.contourf(ks, omegas, np.real(epslls), levels=np.linspace(-extent,extent,20), cmap=matplotlib.cm.RdBu_r, extend='both', alpha=1)
    #contours = plt.contourf(ks, omegas, np.real(dispcontours), levels=np.linspace(-extent,extent,50), cmap=matplotlib.cm.RdBu_r, extend='both', alpha=1)
    for contour in contours.collections: contour.set_antialiased(False)     ## optional: avoid white aliasing (for matplotlib 1.0.1 and older) 
    plt.colorbar().set_ticks(np.arange(-extent, extent+1, 5))                        ## optional: colorbar
if epsll_dispersion:
    plt.contour(ks, omegas, np.real(dispcontours), levels=[1,1], colors='k')      ## optional: plot black contour at zero

## Plot the shape of permittivity and permeability
plt.subplot(1, 2, 1)
plt.plot(eps_clas, omegas, lw=2, c='m', label="$\\varepsilon_r'(\\omega/\\omega_0)$")
plt.plot(mu_clas,  omegas, lw=2, c='y', label="$\\mu_r'(\\omega/\\omega_0)$")
if 'aampli' in locals(): ## account for the optical activity
    plt.plot(activity, omegas, lw=1, c='r', label="$\\gamma'(\\omega/\\omega_0)$")
if 'qampli' in locals(): ## account for the optical activity
    plt.plot(quadrupole, omegas, lw=1, c='b', label="$\\alpha'(\\omega/\\omega_0)$")

#plt.ylim((-0.,2.)); plt.yscale('linear')
plt.xlim((-5.,10.)); plt.xscale('linear')
plt.xlabel(u"relative permittivity $\\varepsilon_r$ and permeability $\\mu_r$"); 
plt.ylabel(u"normalized frequency $\\omega/\\omega_0$"); 
plt.grid(); plt.legend()

## Plot classical dispersion contours
plt.subplot(1, 2, 2)
if classical_dispersion:
    plt.plot(omegas*np.sqrt(eps_clas * mu_clas), omegas, lw=2, c='g', alpha=.5)

#plt.ylim((-0.,3.)); plt.yscale('linear')
plt.xlim((-0.,np.max(ks))); plt.xscale('linear')

## ==== Outputting ====
## Finish the plot + save 
plt.xlabel(u"normalized wavenumber $kc/\\omega_0$"); 
plt.ylabel(u"normalized frequency $\\omega/\\omega_0$"); 
plt.grid()
plt.legend(prop={'size':10}, loc='upper right')
plt.savefig(outname, bbox_inches='tight')

