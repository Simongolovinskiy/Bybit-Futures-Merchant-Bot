import websocket


class WebsocketHandler(websocket.WebSocketApp):
    def __init__(self, url):
        super().__init__(url)
        self.on_open = lambda ws: self._on_open(ws)
        self.on_message = lambda ws, message: self._on_message(message)
        self.on_close = lambda ws: self._on_close(ws)
        self.on_error = lambda ws, ex: self.on_error(ws, ex)

    def _on_message(self, message):
        print(message)

    def _on_open(self, ws):
        ...

    def _on_close(self, ws):
        ...

    def _on_error(self, ws, ex):
        print(ex)
