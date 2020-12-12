#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: seba
"""

import numpy as np
import sys
from astropy.io import fits

size_x = 1000
size_y = 1000

mean = 0.05
sigma = 0.44

sky = np.random.normal(mean,sigma,(size_x,size_y))

hdu_sky = fits.PrimaryHDU() #Fits
hdu_sky.data = sky          #Data del header
hdu_sky.writeto('SkyNoise.fits')

print("Tarea 17 git con programa de la Tarea 3 (Ruido del cielo)")
