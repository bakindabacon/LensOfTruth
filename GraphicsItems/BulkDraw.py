from GraphicsItems.ViewPort import Display
from GraphicsItems.CandleStick import CandleStick
import pandas as pd
from datetime import datetime


#GraphDisplay = Display()
data = pd.read_csv('out.csv').drop(columns=['volume']).head()

def BulkDraw(display,data):
    for index, i in data.iterrows():
        i['timestamp'] = i['timestamp']/1000
        #i['open'] = i['open']/100
        #i['high'] = i['high'] / 100
        #i['low'] = i['low'] / 100
        #i['close'] = i['close'] / 100

        #print(*i.tolist())
        #i['timestamp'] = datetime.fromtimestamp(i['timestamp'] / 1000)
        #print(*i.tolist())
        #print(x)
        display.addPlotItem(CandleStick(*i.tolist()))

#BulkDraw(data)