#!/usr/local/bin/python3.6
# requires sox (brew install sox)
import os, time, datetime, requests
btc_low_threshold = 9000
btc_top_threshold = 12000
eth_low_threshold = 400
eth_top_threshold = 500
duration = 3
freq = 800
headers = {'CB-VERSION':datetime.datetime.now().strftime("%Y-%m-%d")}
session = requests.session()
while 1:
	btc_r = session.get('https://api.coinbase.com/v2/prices/BTC-USD/buy', headers=headers)
	eth_r = session.get('https://api.coinbase.com/v2/prices/ETH-USD/buy', headers=headers)
	print(f'{datetime.datetime.now()} :: {btc_r.json()["data"]["base"]}: {btc_r.json()["data"]["amount"]} && {eth_r.json()["data"]["base"]}: {eth_r.json()["data"]["amount"]}')
	if (float(btc_r.json()["data"]["amount"])>btc_top_threshold) or (float(btc_r.json()["data"]["amount"])<btc_low_threshold) or (float(eth_r.json()["data"]["amount"])>eth_top_threshold) or (float(eth_r.json()["data"]["amount"])<eth_low_threshold):
		if (float(btc_r.json()["data"]["amount"])>btc_top_threshold):
			print('BTC higher than top threshold')
		if (float(btc_r.json()["data"]["amount"])<btc_low_threshold):
			print('BTC lower than bottom threshold')
		if (float(eth_r.json()["data"]["amount"])>eth_top_threshold):
			print('ETH higher than top threshold')
		if (float(eth_r.json()["data"]["amount"])<eth_low_threshold):
			print('ETH lower than bottom threshold')
		os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
	time.sleep(15)
