import ccxt
import sys
import json
import pandas as pd
import numpy as np
import datetime
import time, schedule
import dontshare_config as ds
phemex = ccxt.phemex({
    'enableRateLimit': True,
    'apiKey': ds.testnet_j_KEY,
    'secret': ds.testnet_j_SECRET
})
phemex.set_sandbox_mode(True)

params={'type':'swap','code':'USD'}

def bal():
    print(phemex.fetch_balance())
def mkts():
    markets = phemex.fetch_markets(params=params)
    for n in markets:
        print(n,end='\n')
'''
get order book
'''
markets = pd.DataFrame(data=phemex.fetch_markets(), columns=['id',
'lowercaseId',
'symbol',
'base',
'quote',
'settle',
'baseId',
'quoteId',
'settleId',
'type',
'spot',
'margin',
'swap',
'future',
'option',
'index',
'active',
'contract',
'linear',
'inverse',
'subType',
'taker',
'maker',
'contractSize',
'expiry',
'expiryDatetime',
'strike',
'optionType',
'precision',
'limits',
'created',
'info',
'priceScale',
'valueScale',
'ratioScale'])
markets.to_csv('markets.csv',index=False)

def ob():
    ob = phemex.fetch_order_book('BTC/USD:BTC')
    return ob

def get_bidask(symbol):
    ob = phemex.fetch_l2_order_book(symbol, limit = 100)
    #bids = ob['bids'][:][0] #[0][0] is the price for bids[0], [0][1] is the quantity in the other currency
    #asks = ob['asks'][:][0] if len(ob['asks'])>0 else None
    #print(ob['bids'][:])
    return (ob['bids'])
            #,ob['asks'])
#x = get_bidask('BTC/USD:USD')
#print(x[0],x[1])

#print(ob()['bids'])
from_datetime = '2024-05-25 00:00:00'
from_timestamp = phemex.parse8601(from_datetime)
#print(from_timestamp)
def get_bars():
    print(phemex.has['fetchOHLCV'] == 'emulated')
    if phemex.has['fetchOHLCV'] == 'emulated':
        print(phemex.id, " cannot fetch old historical OHLCVs, because it has['fetchOHLCV'] =",
              phemex.has['fetchOHLCV'])
        sys.exit()
    bars = phemex.fetch_ohlcv(symbol='BTC/USD:BTC', timeframe='1m', limit = 500)
    df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    return df
b = get_bars()
b.to_csv('out.csv', index=False)
b['SMA10'] = b.close.rolling(10).mean()
#print(ob())
