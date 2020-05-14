# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:13:30 2020

@author: Hossein
"""



import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt

spy = pdr.get_data_yahoo('spy',"2002-01-01")
spy['Adj Close'].plot()

daily_return = spy['Adj Close'].pct_change()

daily_return1 = (spy['Adj Close'][1:]/spy['Adj Close'][:-1].values)-1

daily_return1.plot()

plt.figure(figsize=(60,30))
daily_return.plot()

daily_return.hist(bins=10)

mean = daily_return.mean()
std = daily_return.std()
daily_return.hist(bins=30)
plt.axvline(mean , color='w',Linestyle='dashed',linewidth=2)
plt.axvline(std , color='r',Linestyle='dashed',linewidth=2)
plt.axvline(-std , color='r',Linestyle='dashed',linewidth=2)
plt.axvline(daily_return.max() , color='orange',Linestyle='dashed',linewidth=2)
plt.axvline(daily_return.min() , color='orange',Linestyle='dashed',linewidth=2)

daily_return.kurtosis()




