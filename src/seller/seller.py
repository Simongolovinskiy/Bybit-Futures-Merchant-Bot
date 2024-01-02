import json
import threading

from src.parser.parser import Parser
from src.api_handler.api import BybitAPI


class Seller:
    def __init__(self):
        self.rest_client = BybitAPI()

    def get_balance(self):
        response = self.rest_client.create_request(endpoint="/v5/account/wallet-balance", method="GET",
                                                   params=json.dumps({
                                                       "accountType": "UNIFIED"
                                                   }))
        return response

    def send_market_order(self, symbol, volume, side):
        response = self.rest_client.create_request(
            endpoint="/v5/order/create",
            method="POST",
            params=json.dumps({
                "category": "inverse",
                "symbol": symbol,
                "side": side,
                "orderType": "Market",
                "qty": volume,
            })
        )
        return response

    def send_limit_order(self, symbol, volume, side, price):
        response = self.rest_client.create_request(
            endpoint="/v5/order/create",
            method="POST",
            params=json.dumps({
                "category": "inverse",
                "symbol": symbol,
                "side": side,
                "orderType": "Limit",
                "qty": volume,
                "price": price
            })
        )
        return response

