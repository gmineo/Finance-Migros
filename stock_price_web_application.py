# -*- coding: utf-8 -*-
"""Stock Price Web Application.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p3rua_khJ6qJhgjAfCIQf7stAK9TXQfi
"""

API = "api-fxpractice.oanda.com"
STREAM_API = "stream-fxpractice.oanda.com/"
ACCESS_TOKEN = "5d81b0fb10745a8a15b496c9dda27d9c-62890b0e95e5a7d71af63b0575675ddb"
ACCOUNT_ID = "101-004-23311696-001"

import sys
import requests
import json
import numpy as np
import pandas as pd
import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import datetime 
from datetime import date
import streamlit as st
import yfinance as finance
today=date.today()

# Project Details
st.title("SIGNAL")
st.header("PROVA")
# markdown syntax
st.write("""
### XCU
""")
st.sidebar.header("from oanda")

def segnale_xcu (initial, final):
  a=initial
  b=final
  loss=4
  delta_piccolo=0.043
  delta_grande=0.4
  perc=0.008

  delta_price= ((b/a)-1)*100
 
      
  if delta_price < delta_grande and delta_price > delta_piccolo:
        sig= 'BUY'
        
        
        
  elif delta_price > delta_grande:
        sig= 'SELL'
        
        
        
  elif delta_price > 0 and delta_price < delta_piccolo:
        sig= 'SELL'
        
        
  elif delta_price > -delta_grande and delta_price < -delta_piccolo:
        sig= 'SELL'
        
        
        
  elif delta_price < -delta_grande:
        sig= 'BUY'
        
        
        
  elif delta_price < 0 and delta_price > -delta_piccolo:
        sig= 'BUY'
        
  
  return sig



client = oandapyV20.API(access_token=ACCESS_TOKEN)
_from=str(today)+'T05:29:59.000000000Z'
params = {"granularity": "M1","from": _from,"count": 1}

r = instruments.InstrumentsCandles(instrument="XCU_USD", params=params)
client.request(r)
print (r.response)
price_info=r.response
price_info=r.response["candles"][0]["mid"]["c"]

price_ini = float(price_info)
print ('------------------------------')
print ('Initial price: ',price_ini)
print ('------------------------------')



headers = {'Content-Type': 'application/json',
           "Authorization": "Bearer 5d81b0fb10745a8a15b496c9dda27d9c-62890b0e95e5a7d71af63b0575675ddb"}
# Streaming prices
baseurl = 'https://stream-fxpractice.oanda.com/v3/accounts/101-004-23311696-001/pricing/stream'
payload = { 'instruments' : 'XCU_USD', 'price': 'mid'}

r = requests.get(baseurl, params=payload, headers=headers, stream=True)
#print(r.headers)
print('\n')

for line in r.iter_lines():
  try:
    if line:
        response=json.loads(line.decode("utf-8"))
        time=response["time"]
        price_bid=float(response["bids"][0]["price"])
        price_ask=float(response["asks"][0]["price"])
        price=(price_bid+price_ask)/2
        sig=segnale_xcu(price_ini,price)
        delta_price= ((price/price_ini)-1)*100
        #st.write(time, '     ',price, '     delta: ', delta_price, ' --->', f'<br style="color:#008400;font-size:15px;">{sig}</br>' ,  unsafe_allow_html=True)
        #st.markdown(f'{time}, <h1 style="color:#008400;font-size:15px;">{sig}</h1>', unsafe_allow_html=True)
        st.write(f'<b {time}, {price}, 'delta: ', {delta_price}, ' --->', style="color:#008400;font-size:15px;">{sig}</b>' ,  unsafe_allow_html=True)
        
  except:
    pass # doing nothing on exception





