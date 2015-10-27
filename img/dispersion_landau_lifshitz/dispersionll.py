#!/usr/bin/env python
#-*- coding: utf-8 -*-

## Import common moduli
import matplotlib, sys, os, time
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import c, hbar, pi

import argparse
parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('--epsll_contours',       type=int, default=1, help='shall thebe plotted? (set to false to disable)')
parser.add_argument('--epsll_dispersion',     type=int, default=1, help='shall thebe plotted? (set to false to disable) ')
parser.add_argument('--classical_dispersion', type=int, default=1, help='shall thebe plotted? (set to false to disable) ')
parser.add_argument('--eampli',       type=float, default=0.,     help='electric oscillator amplitude (prop to k**0)')
parser.add_argument('--eomega0',      type=float, default=1.,     help='electric oscillator frequency')
parser.add_argument('--egamma',       type=float, default=0.001,  help='electric oscillator frequency')
parser.add_argument('--aampli',       type=float, default=0.,     help='optical activity oscillator amplitude (prop to k**1)')
parser.add_argument('--aomega0',      type=float, default=0.,     help='optical activity oscillator frequency')
parser.add_argument('--agamma',       type=float, default=0.,     help='optical activity oscillator frequency')
parser.add_argument('--mampli',       type=float, default=0.,     help='magnetic oscillator amplitude (prop to k**2)')
parser.add_argument('--momega0',      type=float, default=1.2,    help='magnetic oscillator frequency')
parser.add_argument('--mgamma',       type=float, default=0.001,  help='magnetic oscillator frequency')
parser.add_argument('--qampli',       type=float, default=0.,     help='quartic oscillator amplitude (prop to k**4)')
parser.add_argument('--qomega0',      type=float, default=0.,     help='quartic oscillator frequency')
parser.add_argument('--qgamma',       type=float, default=0.,     help='quartic oscillator frequency')
parser.add_argument('--outname',      type=str,   default="dispersion.pdf",  help='output filename')
args = parser.parse_args()

np.seterr(all='ignore')      ## do not print warnings for negative-number logarithms etc.


## Use LaTeX
matplotlib.rc('text', usetex=True)
matplotlib.rc('font', size=12)
matplotlib.rc('text.latex', preamble = '\usepackage{amsmath}, \usepackage{txfonts}, \usepackage{palatino},')
matplotlib.rc('font',**{'family':'serif','serif':['Computer Modern Roman, Times']})  ## select fonts
plt.figure(figsize=(10,3))

## An exact curve for the analytic solution of a damped oscillator
def lorentz(omega, omega0, gamma, ampli):
    return ampli / (omega0**2 - omega**2 + 1j*omega*gamma) 

## Generate gridded data from a given 2D function (TODO)
ks = np.linspace(0, 3., 400)
omegas = np.linspace(0, 2., 400)

## Generate classical local permittivity and permeability (the same for all wavevectors k)
eps_clas = 1+lorentz(omegas, ampli=args.eampli, omega0=args.eomega0, gamma=args.egamma)
mu_clas  = 1+lorentz(omegas, ampli=args.mampli, omega0=args.momega0, gamma=args.mgamma)
if args.aampli != 0: ## account for the optical activity
    activity = lorentz(omegas, ampli=args.aampli, omega0=args.aomega0, gamma=args.agamma)
if args.qampli != 0: ## account for the fourth-order expansion terms
    quadrupole = lorentz(omegas, ampli=args.qampli, omega0=args.qomega0, gamma=args.qgamma)


epslls = []
dispcontours = []
for k in ks:
    # Conversion to the Landau-Lifshitz permittivity (mu_ll will be identical to 1, then)
    epsll = eps_clas*np.ones_like(ks)   +   (1-1/mu_clas) * k**2 / omegas**2            ## note that this should divided by mu_0 for realistic values
    if args.aampli != 0: ## account for the optical activity
        epsll += activity * k**1
    if args.qampli != 0: ## account for the fourth-order expansion terms
        epsll += quadrupole * k**4
    dispcontour = epsll * omegas**2 / k**2

    epslls.append(epsll)
    dispcontours.append(dispcontour)
epslls = np.array(epslls).T
dispcontours = np.array(dispcontours).T

## Plot the shape of permittivity and permeability
plt.subplot(1, 2, 1)
plt.plot(eps_clas, omegas, lw=2, c='m', label="$\\varepsilon_r'(\\omega/\\omega_0)$")
plt.plot(mu_clas,  omegas, lw=2, c='y', label="$\\mu_r'(\\omega/\\omega_0)$", ls='--' if ('vacuum' in args.outname) else '-')
if args.aampli != 0: ## account for the optical activity
    plt.plot(activity, omegas, lw=1, c='r', label="$\\gamma'(\\omega/\\omega_0)$")
if args.qampli != 0: ## account for the optical activity
    plt.plot(quadrupole, omegas, lw=1, c='b', label="$\\alpha'(\\omega/\\omega_0)$")

#plt.ylim((-0.,2.)); plt.yscale('linear')
plt.xlim((-5.,10.)); plt.xscale('linear')
plt.xlabel(u"relative permittivity $\\varepsilon_r$ and permeability $\\mu_r$"); 
plt.ylabel(u"normalized frequency $\\omega/\\omega_0$"); 
plt.grid(); plt.legend()



## Plot contours for L-L permittivity
plt.subplot(1, 2, 2) 
#extent = max(-np.min(epslls), np.max(epslls))
extent = 20
if args.epsll_contours:
    contours = plt.contourf(ks, omegas, np.real(epslls), levels=np.linspace(-extent,extent,20), cmap=matplotlib.cm.RdBu_r, extend='both', alpha=1)
    #contours = plt.contourf(ks, omegas, np.real(dispcontours), levels=np.linspace(-extent,extent,50), cmap=matplotlib.cm.RdBu_r, extend='both', alpha=1)
    for contour in contours.collections: contour.set_antialiased(False)     ## optional: avoid white aliasing (for matplotlib 1.0.1 and older) 
    plt.colorbar().set_ticks(np.arange(-extent, extent+1, 5))                        ## optional: colorbar

## Plot L-L dispersion contours
if args.epsll_dispersion:
    plt.contour(ks, omegas, np.real(dispcontours), levels=[1,1], linewidth=3, colors='k')      ## optional: plot black contour at zero

## Plot classical dispersion contours
if args.classical_dispersion:
    plt.plot(omegas*np.sqrt(eps_clas * mu_clas), omegas, c='g', lw=1.5, ls='--')

plt.xlim((-0.,np.max(ks))); plt.xscale('linear')
#plt.ylim((-0.,3.)); plt.yscale('linear')


## ==== Outputting ====
## Finish the plot + save 
plt.xlabel(u"normalized wavenumber $kc/\\omega_0$"); 
plt.ylabel(u"normalized frequency $\\omega/\\omega_0$"); 
plt.grid()
plt.legend(prop={'size':10}, loc='upper right')
plt.savefig(args.outname, bbox_inches='tight')

