#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import matplotlib.pyplot as plt
import astropy
import healpy as hp
import pandas as pd
import operator
import pickle
import random


# In[132]:


pi = np.pi
sin = np.sin
cos = np.cos
A=1


x = np.linspace(-pi,pi,100)
y=A*(sin(x)*sin(x))/(25*(1-(24/25)*cos(x))*(1-(24/25)*cos(x)))
plt.figure()
plt.xlabel(r' $\theta$')
plt.ylabel(r' $dP_{\parallel}/d\Omega$')
plt.title(r'$(dP_{\parallel}/d\Omega) \rightarrow \gamma$ = 5')
plt.plot(x,y)

y1=A*(sin(x)*sin(x))/(100*(1-(99/100)*cos(x))*(1-(99/100)*cos(x)))
plt.figure()
plt.xlabel(r' $\theta$')
plt.ylabel(r' $dP_{\parallel}/d\Omega$')
plt.title(r'$(dP_{\parallel}/d\Omega) \rightarrow \gamma$ = 10')
plt.plot(x,y1)

y2=A*(sin(x)*sin(x))/(1000*(1-(999/1000)*cos(x))*(1-(999/1000)*cos(x)))
plt.figure()
plt.xlabel(r' $\theta$')
plt.ylabel(r' $dP_{\parallel}/d\Omega$')
plt.title(r'$(dP_{\parallel}/d\Omega) \rightarrow \gamma$ = 100')
plt.plot(x,y2)

x = np.linspace(-pi,pi,100)
y=(1/(1-(24/25)*cos(x))**4)*(1-((sin(x)**2)*(cos(0)**2))/(25*(1-(24/25)*cos(x))))
plt.figure()
plt.xlabel(r' $\theta$')
plt.ylabel(r' $dP_{\perp}/d\Omega$')
plt.title(r'$(dP_{\perp}/d\Omega) \rightarrow \gamma$ = 5')
plt.plot(x,y,color='red')

x = np.linspace(-pi,pi,100)
y=(1/(1-(99/100)*cos(x))**4)*(1-((sin(x)**2)*(cos(0)**2))/(100*(1-(99/100)*cos(x))))
plt.figure()
plt.xlabel(r' $\theta$')
plt.ylabel(r' $dP_{\perp}/d\Omega$')
plt.title(r'$(dP_{\perp}/d\Omega) \rightarrow \gamma$ = 10')
plt.plot(x,y,color='red')

x = np.linspace(-pi,pi,100)
y=(1/(1-(999/1000)*cos(x))**4)*(1-((sin(x)**2)*(cos(0)**2))/(1000*(1-(999/1000)*cos(x))))
plt.figure()
plt.xlabel(r' $\theta$')
plt.ylabel(r' $dP_{\perp}/d\Omega$')
plt.title(r'$(dP_{\perp}/d\Omega) \rightarrow \gamma$ = 100')
plt.plot(x,y,color='red')


# In[ ]:




