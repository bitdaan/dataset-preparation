from datetime import datetime, timedelta
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def getBitcoinPrice(moment):
    start = datetime.fromisoformat(moment).timestamp() * 1000
    end = (datetime.fromisoformat(moment) +
           timedelta(hours=24)).timestamp() * 1000
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin/history?interval=h1&start=" +
                            str(start) + "&end=" + str(end), headers=headers)
    prices = response.json()["data"]
    if(len(prices) < 24):
        prices = prices + [{"priceUsd": -1}]*(24-len(prices))
    return prices
