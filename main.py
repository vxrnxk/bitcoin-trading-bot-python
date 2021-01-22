import ssl
import json
import websocket


def open(ws):
	print('Opened!')
	json_subscribe = '''
		{	
	    "event": "bts:subscribe",
	    "data": {
	        "channel": "live_trades_btcusd"
	    	}	
		}
	'''
	ws.send(json_subscribe)


def close(ws):
	print('Closed!')


def error(ws, error):
	print('Error!', error)


def msg(ws, menssage):
	menssage = json.loads(menssage)
	price = menssage['data']['price']
	print(price)

	if price > 34950:
		sell()
	elif price < 34950:
		buy()
	else:
		print('Waiting for prices...')


def buy():
	print('Bought!')


def sell():
	print('Sold!')


if __name__ == '__main__':
	ws = websocket.WebSocketApp("wss://ws.bitstamp.net",
								on_open=open,
								on_close=close,
								on_message=msg,
								on_error=error)
	ws.run_forever(sslopt={'cert_regs': ssl.CERT_NONE})