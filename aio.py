import matplotlib.pyplot as plt
import numpy as np
from config import API_KEY,SECRET_KEY
from talib import abstract
from pybit.unified_trading import HTTP
import time

client = HTTP(
    testnet=False,
    api_key=API_KEY,
    api_secret=SECRET_KEY,
)


symbol='NEARUSDT'
threshold_percentage = 0.5
interval=60

#get klines
def get_klines(symbol, interval):
    klines = client.get_kline(category="linear", symbol=symbol, interval=interval)
    klines = klines['result']['list']
    return klines

#price close
def get_close_data(klines):
    close = [float(i[4]) for i in klines]
    close = close[::-1]
    close = np.array(close)
    return close

# print(get_klines(symbol, interval))
#print(get_close_data(get_klines(symbol, interval)))

#indicator SMA
def get_sma(close):
    SMA = abstract.Function('sma')
    data = SMA(close, timeperiod=25)
    return data








