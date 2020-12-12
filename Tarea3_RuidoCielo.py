#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: seba
"""

import numpy as np
import sys
from astropy.io import fits

size_x = 840
size_y = 840

mean = 0.05
sigma = 0.44

sky = np.random.normal(mean,sigma,(size_x,size_y))

hdu_sky = fits.PrimaryHDU()
hdu_sky.data = sky 
hdu_sky.writeto('ruido_cielo2.fits')