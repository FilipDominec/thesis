#!/bin/bash

./dispersionll.py    --epsll_contours 0 --epsll_dispersion 0 --classical_dispersion 1 --outname  "dispersion_vacuum.pdf" \
    --eampli .0 --eomega0 1. --egamma  .001 --mampli .0 --momega0 1.2 --mgamma  .001

./dispersionll.py    --epsll_contours 0 --epsll_dispersion 0 --classical_dispersion 1 --outname  "dispersion_simple_el.pdf" \
    --eampli 1. --eomega0 1. --egamma  .001 --mampli .0 --momega0 1.2 --mgamma  .001

./dispersionll.py    --epsll_contours 0 --epsll_dispersion 1 --classical_dispersion 1 --outname  "dispersion_ll_el.pdf" \
    --eampli 1. --eomega0 1. --egamma  .001 --mampli .0 --momega0 1.2 --mgamma  .001

./dispersionll.py    --epsll_contours 1 --epsll_dispersion 1 --classical_dispersion     1 --outname  "dispersion_ll_mag.pdf" \
    --eampli .0 --eomega0 1. --egamma  .001 --mampli .3 --momega0 1.2 --mgamma  .001

./dispersionll.py    --epsll_contours 1 --epsll_dispersion 1 --classical_dispersion     1 --outname  "dispersion_ll_elmag.pdf" \
    --eampli 1. --eomega0 1. --egamma  .001 --mampli .3 --momega0 1.2 --mgamma  .001


./dispersionll.py --outname  "dispersion_ll_quadrupp.pdf" \
    --eampli 1 --eomega0 1. --egamma  .001 --mampli 0 --momega0 1.2 --mgamma  .001 r-qampli .08 --qomega0 1. --qgamma .01

./dispersionll.py --outname  "dispersion_ll_quadrupn.pdf" \
    --eampli 1 --eomega0 1. --egamma  .001 --mampli 0 --momega0 1.2 --mgamma  .001 --qampli -.08 --qomega0  1. --qgamma  .01

./dispersionll.py --outname  "dispersion_ll_activen.pdf" \
    --eampli 1 --eomega0 1. --egamma  .001 --mampli 0 --momega0 1.2 --mgamma  .001 --aampli -.7 --aomega0 1. --agamma .001

./dispersionll.py --outname  "dispersion_ll_activep.pdf" \
    --eampli 1 --eomega0 1. --egamma  .001 --mampli 0 --momega0 1.2 --mgamma  .001 --aampli .7 --aomega0 1. --agamma .001
