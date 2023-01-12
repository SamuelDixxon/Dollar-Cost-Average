
from datetime import date
import pickle
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


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

    DCAdf['Shares Bought in Week'] = (
        DataNeeded['Close'][0: -1:Frequency]).rdiv(WeeklyContribution)
    DCAdf['Cumulative Shares'] = DCAdf['Shares Bought in Week'].expanding(
    ).sum()


    # Latest Stock Price * Shares accumulated
    Total_Equity = DCAdf['AAPL Price'][-1] * \
        DCAdf['Cumulative Shares'][-1]
    Total_Cost = DCAdf['Contribution Weekly'].sum()
    Total_Profit = Total_Equity-Total_Cost
    LumpSumInvestment = yf.download('AAPL', '2000-2-1', date.today())

    # get the total contribution to the investment account
    Total_Cost = DCAdf['Contribution Weekly'].sum()
    # Total profit over interval
    Total_Profit = (
        Total_Cost / LumpSumInvestment['Close'][0]) * LumpSumInvestment['Close'][-1]

    return Total_Profit


# Dollar Cost Average Function
def DCA_PLOT(WeeklyContribution, InitialInvestmentDay, StockTicker, Frequency):
    """
    WeeklyContribution : Floating-point value indicating the fiscal amount to invest each week
    InitialInvestmentDay: String Value indicating initial day to be investing in the stock market: ex. Jan 1 2020: 2020-1-1
    StockTicker : Enter the ticker of the stock that you are investing into: ex. Tesla: 'TSLA' (rem)
    Frequency : How often you will buy the asset in dollar cost average fashion
    """

    DataNeeded = yf.download(StockTicker, InitialInvestmentDay, date.today())
    print(DataNeeded.head)
    DCAdf = pd.DataFrame(data={"Contribution Weekly": [WeeklyContribution for i in range(0, len(DataNeeded)-1, 5)],
                               str(StockTicker)+" "+"Price": DataNeeded['Close'][0: -1:Frequency]})

    DCAdf['Shares Bought in Week'] = (
        DataNeeded['Close'][0: -1:Frequency]).rdiv(WeeklyContribution)

    plt.scatter(DCAdf.index, DCAdf['Shares Bought in Week'])
    plt.show()
