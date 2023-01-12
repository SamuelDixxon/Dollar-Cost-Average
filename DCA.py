from functions import *
import os
import matplotlib.pyplot as plt

DataOfConcern = DCA(3000, '2022-1-1', 'AAPL', 5)

# our data saved in file for practice
#DataOfConcern.to_pickle(str(os.getcwd()) + "/DollarCostAverage.pkl")

DataOfConcern['Cumulative Shares'] = DataOfConcern['Shares Bought in Week'].expanding().sum()
# Latest Stock Price * Shares accumulated
Total_Equity = DataOfConcern['AAPL Price'][-1] * \
    DataOfConcern['Cumulative Shares'][-1]
Total_Cost = DataOfConcern['Contribution Weekly'].sum()
Total_Profit = Total_Equity-Total_Cost
LumpSumInvestment = yf.download('AAPL', '2000-2-1', date.today())

# get the total contribution to the investment account
Total_Cost = DataOfConcern['Contribution Weekly'].sum()
# Total profit over interval
Total_Profit = (
    Total_Cost / LumpSumInvestment['Close'][0]) * LumpSumInvestment['Close'][-1]

print("Your total profits over investment span are: $", Total_Equity)

DataOfConcern = DCA_PLOT(3000, '2022-1-1', 'AAPL', 5)
