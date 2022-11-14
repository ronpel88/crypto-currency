import urllib.request, json
import time

def get_bitcoin_price():
    with urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json") as url:
        data = json.load(url)
    price = data["bpi"]["USD"]["rate_float"]
    return price