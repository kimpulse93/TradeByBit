import websocket
import threading
import _thread
import json

class SocketConn(websocket.WebSocketApp):
    def __init__(self, url, params=[]):
        super().__init__(url=url, on_open=self.on_open)

        self.params = params
        self.on_message = lambda ws, msg:self.message(msg)
        self.on_error = lambda ws, e: print('Error', e)
        self.on_close = lambda ws: print("Closing")

        self.run_forever()

    def on_open(self,ws,):
        print("WebSocket was opened")

        def run(*args):
            tradeStr = {"op": "subscribe", "args": self.params}
            ws.send(json.dumps(tradeStr))
        _thread.start_new_thread(run,())

    def message(self,msg):
        print(msg)

# kline
threading.Thread(target=SocketConn, args=('wss://stream.bybit.com/v5/public/linear',['kline.1.ETHUSDT'])).start()
#Orderbook
threading.Thread(target=SocketConn, args=('wss://stream.bybit.com/v5/public/linear',['orderbook.50.ETHUSDT'])).start()
# trade
threading.Thread(target=SocketConn, args=('wss://stream.bybit.com/v5/public/linear',['publicTade.ETHUSDT'])).start()