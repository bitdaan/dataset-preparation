import datetime
import ccxt

# get price of bitcoin at the timestamp that is passed to this function .
def getPrice(moment):
    exchange = ccxt.binance()
    timestamp = int(datetime.datetime.strptime(
        moment, "%Y-%m-%d %H:%M:%S%z").timestamp() * 1000)
    response = exchange.fetch_ohlcv('BTC/USDT', '1m', timestamp, 1)
    return response[0][2]
