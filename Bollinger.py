# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:45:01 2020

@author: Hossein
"""

import pandas as pd
import pandas_datareader as pdr

spy = pdr.get_data_yahoo('SPY',"2012-01-01","2012-12-31")


spy['Adj Close'].plot(title='SPY rolling mean',label='SPY')

rm_SPY_mean = spy['Adj Close'].rolling(20).mean()
rm_SPY_std = spy['Adj Close'].rolling(20).std()

rm_SPY_mean.plot()
#rm_SPY_std.plot(color='black')


rm_SPY_upper = rm_SPY_mean + (rm_SPY_std * 2)
rm_SPY_bottom = rm_SPY_mean - (rm_SPY_std * 2)

rm_SPY_upper.plot(color='red')
rm_SPY_bottom.plot(color='blue')
rm_SPY_mean.plot(color='orange')
spy['Adj Close'].plot()







