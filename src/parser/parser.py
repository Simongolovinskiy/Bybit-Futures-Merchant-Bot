from src.api_handler.api import BybitAPI


class Parser:
    def __init__(self):
        self.rest_client = BybitAPI()

    def get_symbol_list(self):

        response = self.rest_client.create_request(endpoint="/v5/market/tickers?category=linear", method="GET")
        return [symbol["symbol"] for symbol in response["result"]["list"]]

    def get_symbol_info(self, symbol):
        response = self.rest_client.create_request(
            endpoint=f"/v5/market/tickers?category=linear&symbol={symbol}",
            method="GET"
        )
        return response["result"]["list"]

