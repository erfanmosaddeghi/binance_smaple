import numpy as np
from numpy import genfromtxt
import talib

data = genfromtxt('./5min_1year.csv',delimiter=',')

close = data[:,4]


mv_avg = talib.SMA(close,timeperiod=25)

for item in mv_avg:
    if item < 10000:
        print(item)

"""
rsi = talib.RSI(close)

for item in rsi:
    print(item)"""