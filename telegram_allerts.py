import requests
import time

TELEGRAM_TOKEN = '---'
TELEGRAM_CHANNEL = '@---'
SYMBOL = 'NEARUSDT'
LEVEL = 2.965

def send_message(text):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TELEGRAM_TOKEN)
    data = {
        'chat_id': TELEGRAM_CHANNEL,
        'text': text
    }
    response = requests.post(url, data=data) 


while True:
    tickers = requests.get(f"https://fapi.binance.com/fapi/v1/trades?symbol={SYMBOL}&limit=1")
    result = tickers.json()
    price = result[0]['price']

    if float(price) > LEVEL:
        text = SYMBOL + '  Price!!! : ' + price
        print(price)
        send_message(text)
    else:
        text = "search"
        send_message(text)
    time.sleep(2)