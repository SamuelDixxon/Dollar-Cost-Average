# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:14:25 2020

@author: Samuel Dixon

Dollar Cost Average Program
"""
from datetime import date
import pandas as pd
import yfinance as yf
import pickle



def get_dframe(ticker, start, stop):
    """
    ticker: the stock ticker of interest, ex. apple: 'AAPL'
    start: start of investment in string format, ex. Jan. 1, 2020: '2020-1-1'
    stop:  current date in string format, ex. Aug. 13, 2020: '2020-8-13'
    Return: Pandas data frame of stock ticker data history
    """
    tickerData = yf.Ticker(str(ticker))
    return tickerData.history(period='1d', start=start, stop=stop)
  


def DCA(WeeklyContribution, InitialInvestmentDay, StockTicker): #Dollar Cost Average Function
    """
    WeeklyContribution : Floating-point value indicating the fiscal amount to invest each week
    InitialInvestmentDay: String Value indicating initial day to be investing in the stock market: ex. Jan 1 2020: 2020-1-1
    StockTicker : Enter the ticker of the stock that you are investing into: ex. Tesla: 'TSLA' (rem)
    """
    DataNeeded = get_dframe(StockTicker, InitialInvestmentDay, date.today)
    Frequency = 5 # period of investing each week remeber market is closed on weekends
    DCAdf = pd.DataFrame(data={"Contribution Weekly": [WeeklyContribution for i in range(0,len(DataNeeded), 5)],str(StockTicker)+" "+"Price":DataNeeded['Close'][0: -1 :Frequency]})
    DCAdf['Number of Shares'] = (DataNeeded['Close'][0: -1 :Frequency]).rdiv(WeeklyContribution)
    
    return DCAdf

DataOfConcern = DCA(3000, '2020-2-1', 'AAPL')

DataOfConcern.to_pickle("C:/Users/15123/Desktop/DollarCostAverage.pkl")

Total_Equity = DataOfConcern['AAPL Price'].tail(1) * DataOfConcern['Number of Shares'].sum()

Total_Cost = DataOfConcern['Contribution Weekly'].sum()

Total_Profit = Total_Equity-Total_Cost

print("Your total profits over investment span are: $", Total_Profit)



    
    
    
    
    
    
    
    