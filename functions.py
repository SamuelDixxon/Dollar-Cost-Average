
from datetime import date
import pickle
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

def DCA(WeeklyContribution, InitialInvestmentDay, StockTicker, Frequency):  # Dollar Cost Average Function
    """
    WeeklyContribution : Floating-point value indicating the fiscal amount to invest each week
    InitialInvestmentDay: String Value indicating initial day to be investing in the stock market: ex. Jan 1 2020: 2020-1-1
    StockTicker : Enter the ticker of the stock that you are investing into: ex. Tesla: 'TSLA' (rem)
    Frequency : How often you will buy the asset in dollar cost average fashion
    """

    DataNeeded = yf.download(StockTicker, InitialInvestmentDay, date.today())
    DCAdf = pd.DataFrame(data={"Contribution Weekly": [WeeklyContribution for i in range(0, len(DataNeeded)-1, 5)], 
                        str(StockTicker)+" "+"Price": DataNeeded['Close'][0: -1:Frequency]})

    DCAdf['Shares Bought in Week'] = (DataNeeded['Close'][0: -1:Frequency]).rdiv(WeeklyContribution)

  
    return DCAdf
