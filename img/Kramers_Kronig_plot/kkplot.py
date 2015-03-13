#!/usr/bin/env python
#-*- coding: utf-8 -*-

## Import common moduli
import matplotlib, sys, os, time, re
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import c, hbar, pi
matplotlib.rc('text', usetex=True)
matplotlib.rc('font', size=10)
matplotlib.rc('text.latex', preamble = '\usepackage{amsmath}, \usepackage{yfonts}, \usepackage{txfonts}, \usepackage{lmodern},')
matplotlib.rc('font',**{'family':'serif','serif':['Computer Modern Roman, Times']})  ## select fonts
#matplotlib.rc('text.latex',unicode=True)   ## use accented letters

damping = 1
frequency = .3
maxfplot = 3.0
time1, time2 = -10*np.pi, 10*np.pi
x = np.linspace(time1, time2, 1600)

yodd  = (np.sin(x*2*np.pi*frequency) * np.exp(-np.abs(x)/np.pi*damping)) * 1/2
yeven = (np.sin(x*2*np.pi*frequency) * np.exp(-np.abs(x)/np.pi*damping)) * np.sign(x)/2
#yodd  = (np.exp(1j*x*2*np.pi*frequency) * np.exp(-np.abs(x)/np.pi*damping)) * 1/2
#yeven = (np.exp(1j*x*2*np.pi*frequency) * np.exp(-np.abs(x)/np.pi*damping)) * np.sign(x)/2
yboth = yodd+yeven

plt.figure(figsize=(11,4))
for rowX, colX, rowF, colF, y, label in  \
        [(0,0,   1,3,   yboth, ('$\\hspace{-5mm}\\text{Re}(f)$', '$\\text{Im}(f)$')),
         (0,1,   1,1,   yodd,  ('$\\text{Re}(f_\mathrm{odd})$', '$\\text{Im}(f_\mathrm{odd})$')),
         (0,2,   1,2,   yeven, ('$\\text{Re}(f_\mathrm{even})$', '$\\text{Im}(f_\mathrm{even})$'))]:
    #zip((0,1,2), (0,1,2), (yodd, yeven, yboth), ('odd', 'even', 'both')):


    ## Column span (whole height by default)
    ax = plt.subplot2grid((2,4), (rowX,colX))
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=1, hspace=.6)


    ## Plot time-domain data
    plt.plot(x, np.real(y), c='#aa0088', label=label[0])
    plt.plot(x, np.imag(y), c='#aa8800', label=label[1], lw=.8)
    plt.ylabel('amplitude')
    plt.xlabel('time')
    plt.xticks((-10,0,10))
    plt.xlim((-14,14))
    plt.ylim((-.5,2))
    plt.legend(prop={'size':8}).draw_frame(False)

    
    ## Fourier transform
    freq    = np.fft.fftfreq(len(x), d=(x[1]-x[0]))         # calculate the frequency axis with proper spacing
    yf      = np.fft.fft(y, axis=0) / len(x) * 2*np.pi      # calculate the FFT values
    freq    = np.fft.fftshift(freq)
    yf     = np.fft.fftshift(yf)
    truncated = np.logical_and(freq>-maxfplot, freq<maxfplot)         # (optional) get the frequency range
    (yf, freq) = map(lambda x: x[truncated], (yf, freq))    # (optional) truncate the data points

    ## Plot frequency-domain data
    ax = plt.subplot2grid((2,4), (rowF, colF))
    plt.plot(freq, np.real(yf / np.exp(1j*time1*2*np.pi*freq)), c='#008844', label=re.sub('f','F',label[0]))
    plt.plot(freq, np.imag(yf / np.exp(1j*time1*2*np.pi*freq)), c='#88aa00', label=re.sub('f','F',label[1]),lw=.8)
    plt.legend(prop={'size':8}).draw_frame(False)
    plt.ylabel('spectral amplitude')
    plt.xlabel('frequency')
    plt.xlim((-1.4,1.4))
    plt.xticks((-1,0,1))
    plt.ylim((-.15,.35))

## Pretty annotate (with text and arrow)
## `xycoords' and `textcoords' can be chosen from  {offset|figure|axes}:{points|pixels|fraction} | data
col = '#00aaff'
arrowprops  = dict(arrowstyle=('->', '-|>', 'simple', 'fancy')[0], connectionstyle = 'arc3,rad=0', lw=1, ec=col, fc=col)
plt.annotate('',                    
        xy      = (.37, .45),    xycoords  ='figure fraction',
        xytext  = (.37, .55),    textcoords='figure fraction', 
        arrowprops  = arrowprops,       )
plt.annotate('FT',                    # set empty to disable text
        xy      = (.39,  .5),    xycoords  ='figure fraction',
        ha='left', va='center', size=25, color=col,)
plt.annotate('',                    
        xy      = (.63, .45),    xycoords  ='figure fraction',
        xytext  = (.63, .55),    textcoords='figure fraction', 
        arrowprops  = arrowprops,       )
plt.annotate('FT',                    
        xy      = (.65,  .5),    xycoords  ='figure fraction',
        ha='left', va='center', size=25, color=col,)

plt.annotate('=',                    
        xy      = (.24,  .80),    xycoords  ='figure fraction',
        ha='center', va='center', size=45, color=col,)
plt.annotate('+',                   
        xy      = (.5,  .80),    xycoords  ='figure fraction',
        ha='center', va='center', size=45, color=col,)
plt.annotate('+',                  
        xy      = (.5,  .27),    xycoords  ='figure fraction',
        ha='center', va='center', size=45, color=col,)
plt.annotate('=',                 
        xy      = (.76,  .27),    xycoords  ='figure fraction',
        ha='center', va='center', size=45, color=col,)

#plt.show()
plt.savefig("kk_new.pdf", bbox_inches='tight')
