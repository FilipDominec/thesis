#!/bin/bash

sharedoptions='*dat --paramname comment --figsizey 3 --xlim2 1. --usetex yes'

cellsize=60e-6
~/p/MEEP_2014/plot_multiline.py $sharedoptions --xlabel "Frequency (THz)" --ycol 'real N' --y2eval '0-y2' \
    --ycol2 'imag N' --ylim1 -1.2 --ylim2 2\
	--paramlabel '%s' --ylabel 'Refractive index $N_{\text{eff}}$' --output ${PWD##*/}_n.pdf  \
    --overlayplot "c/2/$cellsize/x/1e12,-c/2/$cellsize/x/1e12,2*c/2/$cellsize/x/1e12"  
#
~/p/MEEP_2014/plot_multiline.py $sharedoptions --xlabel "Frequency (THz)" --ycol 'real mu' --y2eval '0-y2' \
    --ycol2 'imag mu' --ylim1 -1.2 --ylim2 2\
	--paramlabel '%s' --ylabel 'Permeability $\mu_{\text{eff}}$' --output ${PWD##*/}_mu.pdf 

~/p/MEEP_2014/plot_multiline.py $sharedoptions --xlabel "Frequency (THz)" --ycol 'real eps' --y2eval '0-y2' \
    --ycol2 'imag eps' --ylim1 -1.8 --ylim2 2.6\
	--paramlabel '%s' --ylabel 'Permittivity $\varepsilon_{\text{eff}}$' --output ${PWD##*/}_eps.pdf 
