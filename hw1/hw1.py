#PHYA 201
#Alyssa Johnson
#Homework 1

import scipy as sy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import dblquad

#constants
h = 6.626e-34       # Planck's constant
c = 3.0e+8          # speed of light (m/s)
k = 1.38e-23        # Boltzmann constant
pi = np.pi
T = range (1,8000)
SB = 5.67e-5
b = 2.89e-3


##################
# Question 2f
##################
#Power = Flux x Area
# Flux = (sigma) * T^4

#1. Thermal flux from your skin
def skin_flux(TempSkin):
    print('1. Thermal flux from your skin')
    return  SB * (TempSkin**4)

#2. Total thermal power radiated by me
def me_power(sk_flux, me_area):
    print('2. Total thermal power radiated')
    return sk_flux * me_area

#3. Peak Wavelength of your blackbody emission
def me_peak(T):
    print('3. Peak Wavelength of your blackbody emission')
    return b/T

#5. Thermal Flux from Sun's surface
def sun_flux(T):
    print('5. Thermal Flux from Suns surface')
    return SB * T**4

print(skin_flux(305))
print(me_power(490661.9904375,1.6))
print(me_peak(305))
print(sun_flux(5772))


