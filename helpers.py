import threading
import urllib.request, json
from socket import timeout
import configparser
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

config = configparser.ConfigParser()
config.read('config.ini')
interval = int(config['DEFAULT']['interval'])
average_window_minutes = int(config['DEFAULT']['average_window_minutes'])
crypto_api_url = str(config['DEFAULT']['crypto_api_url'])
currency = str(config['DEFAULT']['currency'])

prices = []

def get_price():
    try:
        response = urllib.request.urlopen(crypto_api_url, timeout=interval)
        data = json.load(response)
        price = data["bpi"][currency]["rate_float"]
    except timeout:
        price = -1
    print("[DEBUG] current price: ", price)
    return price


def append_price(price):
    if (len(prices) == (average_window_minutes * 60) / interval):
        prices.pop(0)
    prices.append(price)


def calc_average():
    threading.Timer(interval, calc_average).start()
    price = get_price()
    if price == -1:
        price = prices[-1]
    append_price(price)
    print("[DEBUG] prices= ", prices)
    average = sum(prices) / len(prices)
    print("[DEBUG] average= ", average)
    return average
