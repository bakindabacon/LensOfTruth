import datetime
import matplotlib.pyplot as plt
import backtrader as bt
import pandas as pd
import backtrader.indicators as btind
import backtrader.feeds as btfeeds
import strategies as stg



# nflx = pd.read_csv('NFLX.csv')

cerebro = bt.Cerebro()
# print(cerebro.broker.getvalue())
cerebro.broker.setcash(10000000)
print('Initial Portfolio Value %.2f' % cerebro.broker.getvalue())

data = btfeeds.YahooFinanceCSVData(dataname='MCD.csv', fromdate=datetime.datetime(2023, 4, 20),
                                   todate=datetime.datetime(2024, 4, 10))
cerebro.adddata(data)
cerebro.addstrategy(stg.TestStrategy)
cerebro.addsizer(bt.sizers.FixedSize, stake=1000)

cerebro.run()
print('Final Portfolio Value %.2f' % cerebro.broker.getvalue())
cerebro.plot()