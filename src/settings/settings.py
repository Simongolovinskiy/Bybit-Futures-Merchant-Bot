import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "../.env"))


class SettingsManager:

    @staticmethod
    def get_api_key():
        return os.environ.get("api_key")

    @staticmethod
    def get_api_secret():
        return os.environ.get("api_secret")

    @staticmethod
    def get_testnet_url():
        return os.environ.get("url_testnet")

    @staticmethod
    def get_url():
        return os.environ.get("url")
