# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:13:30 2020

@author: Hossein
"""



import pandas as pd
import pandas_datareader as pdr

spy = pdr.get_data_yahoo('SPY',"2012-01-01","2012-12-31")


daily_return = spy['Adj Close'].pct_change()

daily_return1 = (spy['Adj Close'][1:]/spy['Adj Close'][:-1].values)-1

daily_return1.plot()

daily_return.plot()

