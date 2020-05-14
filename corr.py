# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:54:46 2020

@author: Hossein
"""



import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import numpy as np

gld = pdr.get_data_yahoo('GLD')['Adj Close']
spy = pdr.get_data_yahoo('SPY')['Adj Close']
xom = pdr.get_data_yahoo('XOM')['Adj Close']

gld_daily = gld.pct_change().dropna()
spy_daily = spy.pct_change().dropna()
xom_daily = xom.pct_change().dropna()





plt.scatter(x=spy_daily,y=xom_daily)
plt.xlabel('SPY')
plt.ylabel('XOM')


plt.scatter(x=spy_daily,y=gld_daily)
plt.xlabel('SPY')
plt.ylabel('GLD')


beta_XOM , alpha_XOM = np.polyfit(spy_daily , xom_daily ,1)
beta_GLD , alpha_GLD = np.polyfit(spy_daily , gld_daily , 1)


plt.plot(spy_daily,beta_XOM*spy_daily+alpha_XOM,'-',color='r')
plt.scatter(x=spy_daily,y=xom_daily)
plt.xlabel('SPY')
plt.ylabel('XOM')


plt.plot(spy_daily,beta_GLD*spy_daily+alpha_GLD,'--',color='r')
plt.scatter(x=spy_daily,y=gld_daily)
plt.xlabel('SPY')
plt.ylabel('GLD')





