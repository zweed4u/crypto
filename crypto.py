#!/usr/local/bin/python3.6
import time, datetime, requests
headers = {'CB-VERSION':datetime.datetime.now().strftime("%Y-%m-%d")}
session = requests.session()
while 1:
	btc_r = session.get('https://api.coinbase.com/v2/prices/BTC-USD/buy', headers=headers)
	print(f'{datetime.datetime.now()} :: {btc_r.json()["data"]}')
	eth_r = session.get('https://api.coinbase.com/v2/prices/ETH-USD/buy', headers=headers)
	print(f'{datetime.datetime.now()} :: {eth_r.json()["data"]}')
	print()
	time.sleep(15)
