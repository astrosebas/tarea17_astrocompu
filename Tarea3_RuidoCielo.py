#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: seba
"""
#Importando paqueterías
import numpy as NP
import sys
from astropy.io import FITS

size_x = 1000 #Tamaño de la imagen en x
size_y = 1000 #Tamaño de la imagen en y

mean = 0.05
sigma = 0.44

sky = NP.random.normal(mean,sigma,(size_x,size_y))

hdu_sky = FITS.PrimaryHDU() #Fits
hdu_sky.data = sky          #Data del header
hdu_sky.writeto('SkyNoise.fits')

print("Tarea 17 git con programa de la Tarea 3 (Ruido del cielo)")

def Msj(X):
   print(X)

print("hola")
