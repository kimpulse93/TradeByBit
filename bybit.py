import requests

# Получить информацию об инструментах
instruments_info = requests.get('https://api.bybit.com/v5/market/instruments-info?category=spot')
result = instruments_info.json()
print(result)


# Получить свечи
klines = requests.get('https://api.bybit.com/v5/market/kline?category=spot&symbol=BTCUSDT&interval=D')
result = klines.json()
print(result)


# Получить ордербук
orderbook = requests.get('https://api.bybit.com/v5/market/orderbook?category=spot&symbol=BTCUSDT')
result = orderbook.json()
print(result)


# Получить тикер
tickers = requests.get('https://api.bybit.com/v5/market/tickers?category=spot')
result = tickers.json()
print(result)