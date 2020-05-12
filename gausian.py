# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:18:41 2020

@author: Hossein
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.signal import wiener, filtfilt, butter, gaussian, freqz
from scipy.ndimage import gaussian_filter1d
import math
import pandas_datareader as pdr
from scipy.ndimage import filters
import pandas as pd



b = gaussian(M=80,std=5)

plt.plot(b)

gld = pdr.get_data_yahoo('GLD',"2016-11-08")
#plt.plot(gld['High'])
gld = gld['High']


ga = filters.convolve(gld , b/b.sum(),'same')
ga = np.convolve(gld , b/b.sum(),'valid')

ga = pd.DataFrame(ga)

#ga.index = gld.index
plt.figure(figsize=(50,25))
plt.plot(ga,label='Gaussian smoothing effect')
plt.plot(gld,label='GLD High')


#srate = 1000
#time = 0:1/srate:3



"""
srate = 1000
#full width half maximum : the key gaussian parameter
fwhm = 25 #in ms
#normalized time vector in ms
k = np.arange(-100,101)
gtime = 1000*k/srate

gauswin =[]

for i in gtime:
    gauswin.append(math.exp( -(4*math.log(2)*i**2) /fwhm**2))


plt.plot(gtime,gauswin)
"""














