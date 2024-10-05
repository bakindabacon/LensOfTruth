import websocket
import json
import asyncio
from datetime import datetime
import Exchange.dontshare_config as ds
expire_time=int(datetime.now().timestamp()+120)

# Define the websocket URL
ws_url = 'wss://testnet-api.phemex.com/ws'

# Define the authentication credentials
api_key = ds.testnet_j_KEY
api_secret = ds.testnet_j_SECRET
# Define the user authentication request payload
auth_payload = {
  "method": "user.auth",
  "params": [
    "API",
    api_key,
    api_secret,
    expire_time
  ],
  "id": 0
}

# Define the subscribe orderbook request payload
orderbook_subscribe_payload = {
    "id": 1,
    "method": "orderbook.subscribe",
    "params": ["sBTCUSDT",True]
}

trades_subscribe_payload = {
    "id": 1,
    "method": "trade.subscribe",
    "params": ["sBTCUSDT"]
}

#ping_payload = {
   # "method": "server.ping"
    #"params": []
#}

# Define the on_message function to handle incoming messages
#websocket.enableTrace(True)

def format_data(data):

    if 'book' in data.keys():
        d = data['book']
        print("order book:", end='\n')
        #print(d.keys())
        #print(d.values()[0])
        for item in d.values():
            #print (item.key())
            if len(item) != 0:

                ([[i[0] / 10 ** 8, i[1] / 10 ** 3] for i in item])
                #print([[i[0], i[1]] for i in item],end='\n')
        return order_book
           #print([[type(datetime.fromtimestamp(i[0]))]])
                #print(item)


    elif 'trades' in data.keys():
        d=data['trades']
        print("recent orders")


        for i in d:
        # print(type(item))
            if len(i) != 0:

           #print([[type(datetime.fromtimestamp(i[0]))]])

                print([[i[1], i[2] / 10 ** 8, i[3] / 10 ** 3]])
def on_message(ws, message):

    data = json.loads(message)
    #print(data.keys())
    #print(data.keys())
    print(format_data(data))
        #for item in trade_data:
            #print(item)
# Define the on_open function to send authentication and subscribe requests
def on_open(ws):
    # Send user authentication request
    #print(json.dumps(auth_payload))
    #ws.send(json.dumps(auth_payload))

    # Send orderbook subscribe request
    ws.send(json.dumps(orderbook_subscribe_payload))

    ws.send(json.dumps(trades_subscribe_payload))

# Establish the websocket connection
ws = websocket.WebSocketApp(ws_url, on_open = on_open, on_message=on_message)
# Run the websocket connection
ws.run_forever(ping_interval=5, ping_timeout=4)