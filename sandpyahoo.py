import yfinance as yfinance
start_date =  '1970-01-10'
end_date = '2024-07-09'
ticker = '^GSPC'
data = yfinance.download(ticker,start_date, end_date)
print(data.tail())

data.to_csv(F"{ticker}.csv")