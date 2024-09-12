import json
import traceback
import websocket
import threading

class Socket_conn_Binance(websocket.WebSocketApp):
    def __init__(self, url):
        super().__init__(
            url=url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.run_forever()

    def on_open(self, ws):
        print(ws, 'Websocket was opened')

    def on_error(self, ws, error):
        print('on_error', ws, error)
        print(traceback.format_exc())
        exit()

    def on_close(self, ws, status, msg):
        print('on_close', ws, status, msg)
        exit()

    def on_message(self, ws, msg):
        data = json.loads(msg)
        # close = data['p']
        print(data)

url = 'wss://stream.binance.com:443/ws/ethusdt@trade'
# url = 'wss://stream.binance.com:443/ws/ethusdt@trade'
# url = 'wss://stream.binance.com:443/ws/ethusdt@kline_1m'
# url = 'wss://stream.binance.com:443/stream?streams=ethusdt@trade/ethusdt@kline_1m'       
        


threading.Thread(target=Socket_conn_Binance, args=(url,)).start()
