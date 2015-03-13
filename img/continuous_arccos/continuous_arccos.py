#!/usr/bin/env python
#-*- coding: utf-8 -*-
## == Initialization ==



## Import common moduli
import numpy as np
from scipy.constants import c, hbar, pi
import matplotlib
import matplotlib.cm as cm
matplotlib.rc('text', usetex=True)
matplotlib.rc('font', size=11)


## == Define  ==
plot_contours = True
#plot_contours = False
t = np.linspace(-2.3, 2*np.pi+1.8, 1000)
def ffunc(x):
    #the function to be analyzed
    fr = (x-np.pi)*.8 - (x-np.pi)**2 * .02 - (x-np.pi)**3 * .014 - (x-np.pi)**5 * .04*.01
    fi = np.sin(x) * 1.6
    return fr+1j*fi
f = ffunc(t)



matplotlib.rc('text.latex', preamble = \
        '\usepackage{amsmath}, \usepackage{yfonts}, \usepackage{txfonts}, \usepackage{lmodern},')
matplotlib.rc('font',**{'family':'serif','serif':['palatino, times']})  ## select fonts    \usepackage{palatino}, 
## LaTeX options
#matplotlib.rc('font',**{'family':'serif','serif':['Computer Modern Roman, Times']})  ## select fonts
#matplotlib.rc('text.latex',unicode=True)   ## use accented letters

import matplotlib.pyplot as plt
##Start figure + subplot (interactive)


if plot_contours:
    fig = plt.figure(figsize=(4,2))
    ## Plot real contours#{{{
    ax = plt.subplot(131, axisbg='w', aspect=1.0)
    xr = np.linspace(-3,3,100)
    yr = np.linspace(-3,3,100)
    xm, ym = np.meshgrid(xr,yr)
    z =  np.array(map(lambda p: np.arccos(p).real, xm+1j*ym))
    plt.contourf(xr,yr, z, levels=np.arange(-3.15,3.20,.1), colormap=cm.jet, alpha=.3) 
    plt.clabel(
            plt.contour(xr, yr, z/np.pi, levels=np.arange(-1.00, 1.001,.1), lw=5, colors='k'), 
            fmt='$%.1f \\pi$')
    ## Branch cuts
    plt.plot([-1000,-1], [0,0], lw=2, marker='o', c='k')
    plt.plot([1,1000], [0,0], lw=2, marker='o', c='k')
    plt.xlim((-3,3))

    plt.ylabel(u"$\\mathrm{Im}(v)$"); plt.xlabel(u"$\\mathrm{Re}(v)$"); 
    plt.title(u"$\\mathrm{Re}\\arccos(v)$"); 
    #plt.colorbar()

    ## Plot the test function
    plt.plot(np.real(f), np.imag(f), lw=2, c='k') 

    #}}}

    ## Plot imaginary contours #{{{
    ax = plt.subplot(132, axisbg='w', aspect=1.0)
    fig.subplots_adjust(left=.05, bottom=.05, right=.99, top=.99, wspace=.15, hspace=.15)
    xr = np.linspace(-3,3,100)
    yr = np.linspace(-3,3,100)
    xm, ym = np.meshgrid(xr,yr)
    z =  map(lambda p: np.arccos(p).imag, xm+1j*ym)
    plt.contourf(xr,yr, z, levels=np.arange(-3.15,3.20,.1), colormap=cm.jet, alpha=.3) 
    plt.clabel(
            plt.contour(xr, yr, z, levels=np.arange(-3.00, 3.001,.25), lw=5, colors='k'), 
            fmt='$%.2f$')

    ## Branch cuts
    plt.plot([-1000,-1], [0,0], lw=2, marker='o', c='k')
    plt.plot([1,1000], [0,0], lw=2, marker='o', c='k')
    plt.xlim((-3,3))

    ## Plot the test function
    plt.plot(np.real(f), np.imag(f), lw=2, c='k') 
    for pt in [0,2*np.pi]:
        plt.plot(np.real(ffunc(pt)), np.imag(ffunc(pt)), lw=1, c='y', marker='s') 
        #plt.plot(-2,2, lw=1, c='y', marker='s') 
    #}}}
    ## Finish the graph + save 
    plt.title(u"$\\mathrm{Im}\\arccos(v)$"); 
    plt.xlabel(u"$\\mathrm{Re}(v)$"); 
    plt.legend(prop={'size':10}, loc='upper right')
    print 'Contours plotted'
else:
    fig = plt.figure(figsize=(4,5))
    ax1 = plt.subplot(411, axisbg='w')
    plt.plot(t, np.real(f), ls='-', c='k', label='real')
    plt.plot(t, np.imag(f), ls='--', c='k', label='imag')
    plt.xlim((-3,16))
    plt.ylabel('$v(f)$')
    plt.yticks([-1,0,1])
    plt.grid()
    plt.legend()

    ax = plt.subplot(412, axisbg='w',  sharex=ax1)
    F = np.arccos(f)
    plt.plot(t, np.real(F), ls='-', c='b',  label='real')
    plt.plot(t, np.imag(F), ls='--', c='b', label='imag')
    plt.xlim((-3,16))
    plt.ylabel('$\\arccos v$')
    plt.grid()
    plt.legend()

    ax = plt.subplot(413, axisbg='w',  sharex=ax1)
    br = -((np.sign(t)-1)/2)*(2*np.pi) + 2*2*np.pi
    plt.plot(t, br/2/np.pi, ls='-', c='g', label='$\\frac{\\text{branch}}{2\\pi}$') # branch
    si = np.sign(np.imag(F)) * np.sign(t-np.pi)
    plt.plot(t, si, ls='-', c='r', label='sign') # sign
    plt.ylabel('branch, sign')
    plt.ylim((-1.5,3.5))
    plt.xlim((-3,16))
    plt.grid()
    plt.legend()

    ax = plt.subplot(414, axisbg='w',  sharex=ax1)
    F2 = F*si + br
    plt.plot(t, np.real(F2), ls='-', c='m', label='real') # sign
    plt.plot(t, np.imag(F2), ls='--', c='m', label='imag') # sign
    plt.xlim((-3,16))
    plt.ylabel('$\\arccos_{\mathrm{(cont)}} v$')
    plt.grid()
    plt.legend()

    ## Finish the graph + save 
    #plt.title(u"$\\mathrm{Im}\\arccos(v)$"); 

    plt.xlabel(u"Frequency $f$"); 
    plt.legend(prop={'size':10}, loc='upper right')

plt.savefig("continuous_arccos_%s.pdf" % ('contour' if plot_contours else 'graphs'), bbox_inches='tight')

