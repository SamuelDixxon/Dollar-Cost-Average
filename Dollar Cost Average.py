from functions import *
import os

DataOfConcern = DCA(3000, '2022-1-1', 'AAPL', 5)

DataOfConcern.to_pickle(str(os.getcwd()) + "/DollarCostAverage.pkl")  # our data saved in file for practice

DataOfConcern['Cumulative Shares'] = DataOfConcern['Shares Bought in Week'].expanding().sum()
Total_Equity = DataOfConcern['AAPL Price'][-1] * DataOfConcern['Cumulative Shares'][-1] # Latest Stock Price * Shares accumulated
Total_Cost = DataOfConcern['Contribution Weekly'].sum() # 
Total_Profit = Total_Equity-Total_Cost
LumpSumInvestment = yf.download('AAPL', '2000-2-1', date.today())

Total_Cost = DataOfConcern['Contribution Weekly'].sum() # get the total contribution to the investment account
Total_Profit = (Total_Cost / LumpSumInvestment['Close'][0]) * LumpSumInvestment['Close'][-1] #

print("Your total profits over investment span are: $", Total_Equity)


