from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
from backtrader.dataseries import TimeFrame


class RSIStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=15)

    def next(self):
        if self.rsi < 32 and not self.position:
            self.buy(size=1)
        if self.rsi > 69 and self.position:
            self.close()


if __name__ == "__main__":
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(10000)

    data = bt.feeds.GenericCSVData(dataname="15min_2020.csv",timeframe=TimeFrame.Minutes,compression=15,dtformat=2)
    
    cerebro.adddata(data)
    cerebro.addstrategy(RSIStrategy)
    print("Starting Value -> {}".format(cerebro.broker.getvalue()))
    cerebro.run()
    print("Final Value -> {}".format(cerebro.broker.getvalue()))
    #cerebro.plot()