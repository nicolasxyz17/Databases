### YahooFinance Database

import datetime as dt
import os.path
import pandas as pd 
import yfinance as yf

today = dt.date.today()

if today.weekday() in range(0,6):
    print(True)
    
    # Ticker Single Assets List
    symbols = ['SPY','IVV','VOO','VTI','VEA','IEFA','VWO','IEMG']
    
    if os.path.isfile("ETF.xlsx"):
        print(True)
        df = pd.read_excel("ETF.xlsx").set_index('Date')
        #Updating for single assets
        lastDate = df.index[-1]
        priceUpdate = []
        
        for symbol in symbols:
            price = yf.download(symbol,start=lastDate,interval='1d')['Adj Close'].to_frame(symbol)
            priceUpdate.append(price)
        
        update = pd.concat(priceUpdate,axis=1)
        update.columns = symbols
        Adj_prices = pd.concat([df,update],axis=0)
        Adj_prices.to_excel("ETF.xlsx")
                
    else:
        Dataset = []
        
        for symbol in symbols:
            price = yf.download(symbol,start=dt.datetime(1990,1,1),interval='1d')['Adj Close'].to_frame(symbol)
            Dataset.append(price)

        Adj_prices = pd.concat(Dataset,axis=1)
        Adj_prices.columns = symbols
        Adj_prices.to_excel("ETF.xlsx") 
       





