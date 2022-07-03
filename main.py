# QuantBook Analysis Tool 
# For more information see [https://www.quantconnect.com/docs/research/overview]
                            
import seaborn as sns
import random as randm

qb = QuantBook()


tickers = ["TSLA","AAPL","GOGL","MSFT"]

symbols = [qb.AddEquity(ticker,Resolution.Daily).Symbol for ticker in tickers]

history = qb.History(symbols,360,Resolution.Daily)

plt.style.use("seaborn")
plt.figure(figsize=(24,8))

selectedStock = "TSLA"
for s in tickers:
    if s != selectedStock:
      a = plt.scatter(history.loc[selectedStock]["close"].pct_change(),history.loc[s]["close"].pct_change(),alpha=0.75,label=s)
     
plt.legend(loc="upper left", title=f"{selectedStock} vs ?")
plt.xlabel(f"Daily Return ({selectedStock})")
plt.ylabel("Daily Return")
