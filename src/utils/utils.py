import hashlib
import hmac
import time
import urllib3
import requests

from urllib.parse import quote_plus, urlencode

from src.settings.settings import SettingsManager


def bybit_balance(AccessKey: str, SecretKey: str) -> dict:
    params = {
        "api_key": AccessKey,
        "timestamp": round(time.time() * 1000),
        "recv_window": 10000,
        "accountType": "CONTRACT"
    }

    # Create the param str
    param_str = urlencode(
        sorted(params.items(), key=lambda tup: tup[0])
    )

    # Generate the signature
    hash = hmac.new(
        bytes(SecretKey, "utf-8"),
        param_str.encode("utf-8"),
        hashlib.sha256
    )

    signature = hash.hexdigest()
    sign_real = {
        "sign": signature
    }

    param_str = quote_plus(param_str, safe="=&")
    full_param_str = f"{param_str}&sign={sign_real['sign']}"

    # Request information
    url = f"{SettingsManager.get_url()}/v5/account/wallet-balance"
    headers = {"Content-Type": "application/json"}

    body = dict(params, **sign_real)
    urllib3.disable_warnings()

    response = requests.get(f"{url}?{full_param_str}", headers=headers, verify=False).json()

    return response

