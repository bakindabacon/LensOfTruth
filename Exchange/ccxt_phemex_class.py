import ccxt
import json
import pandas as pd
import numpy as np
import datetime
import time, schedule
import Exchange.dontshare_config as ds

class TradeSession:
    def __init__(self):

        self.phemex = ccxt.phemex({
            'enableRateLimit': True,
            'apiKey': ds.testnet_j_KEY,
            'secret': ds.testnet_j_SECRET
        })
        #self.phemex.set_sandbox_mode(True)

        self.params={'type':'swap','code':'USD'}

    def bal(self):
        print(self.phemex.fetch_balance())
    def mkts(self):
        markets = self.phemex.fetch_markets(params=self.params)
        for n in markets:
            print(n,end='\n')
    '''
    get order book
    '''

    def ob(self):
        ob = self.phemex.fetch_order_book('BTC/USD:BTC')
        return ob

    def get_bidask(self, symbol,size):
        ob = self.phemex.fetch_l2_order_book(symbol, limit=size)
        bids = ob['bids'] #[0][0] is the price for bids[0], [0][1] is the quantity in the other currency
        asks = ob['asks']
        return bids, asks

#print(ob()['bids'])

    def get_bars(self,timeframe):
        bars = self.phemex.fetch_ohlcv('BTC/USD:BTC', timeframe = timeframe, limit=500)
        df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        return df

#t = TradeSession()

#x = t.get_bidask('uBTCUSD')
#print(x[0],x[1])


#b = t.get_bars()
#b.to_csv('out.csv', index=False)
#['SMA10'] = b.close.rolling(10).mean()
#print(b)


