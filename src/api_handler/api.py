import time
import hmac
import hashlib
from urllib.parse import urlencode, quote_plus

import urllib3

import requests

from src.settings.settings import SettingsManager


class BybitAPI:
    def __init__(self, testnet=True):
        self.__api_key = SettingsManager.get_api_key()
        self.__api_secret = SettingsManager.get_api_secret()
        if testnet:
            self.bybit_endpoint_url = SettingsManager.get_testnet_url()
        else:
            self.bybit_endpoint_url = SettingsManager.get_url()

    def HTTP_Request(self, endpoint, method, payload):
        recv_window = str(5000)
        time_stamp = str(int(time.time() * 10 ** 3))
        signature = self.genSignature(payload, time_stamp, recv_window)
        headers = {
            'X-BAPI-API-KEY': self.__api_key,
            'X-BAPI-SIGN': signature,
            'X-BAPI-SIGN-TYPE': '2',
            'X-BAPI-TIMESTAMP': time_stamp,
            'X-BAPI-RECV-WINDOW': recv_window,
            'Content-Type': 'application/json'
        }
        url = self.bybit_endpoint_url + endpoint
        try:
            if method == "POST":
                response = requests.post(url, headers=headers, data=payload)
            else:
                response = requests.get(url, headers=headers, params=payload)

            response.raise_for_status()
            response_data = response.json()
            return response_data
        except requests.exceptions.RequestException as e:
            import traceback
            traceback.print_exception(e)

    def genSignature(self, payload, time_stamp, recv_window):
        param_str = str(time_stamp) + self.__api_key + recv_window + payload
        hash = hmac.new(bytes(self.__api_secret, "utf-8"), param_str.encode("utf-8"), hashlib.sha256)
        signature = hash.hexdigest()
        return signature

    def create_request(self, endpoint, method, params=''):
        return self.HTTP_Request(endpoint, method, params)
