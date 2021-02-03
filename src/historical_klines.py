import csv
from operator import delitem
from binance.client import Client
from binance.enums import *
import config



cli = Client(config.API_KEY,config.API_SECRET)

#historicalData = cli.get_historical_klines('BTCUSDT',KLINE_INTERVAL_5MINUTE, "1 year ago UTC")
historicalData = cli.get_historical_klines('BTCUSDT',KLINE_INTERVAL_15MINUTE, "1 Jul 2020","1 Jul 2021")
file = open('15min_2020.csv','w',newline='')
candlesick_writer = csv.writer(file,delimiter=',')

try:
    for candle in historicalData:
        candle[0] = candle[0] / 1000
        candlesick_writer.writerow(candle)

except Exception as e:
    print("ERROR IN -> {}".format(e))

file.close()