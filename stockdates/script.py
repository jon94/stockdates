sudo apt update
sudo apt upgrade

sudo apt install python3

sudo apt install python3-pip


pip3 install yfinance


import yfinance as yf

# Create a Ticker object for the desired stock (e.g., NFLX for Netflix)
stock = yf.Ticker("ADBE")

# Get earnings information for the stock

cal = stock.calendar

if 'Earnings Date' in cal:
earnings_date = cal['Earnings Date'][0] # Extract the first date from the list
print(earnings_date)
else:
print('Earnings date not found.')



import yfinance as yf

# List of stocks to track
stocks = ["ADBE", "AAPL", "MSFT"] # Example list of stocks

# Iterate over each stock
for stock_symbol in stocks:
# Create a Ticker object for the stock
stock = yf.Ticker(stock_symbol)

# Get earnings information for the stock
cal = stock.calendar

# Check if 'Earnings Date' key exists in the earnings information
if 'Earnings Date' in cal:
# Extract earnings dates list
earnings_dates = cal['Earnings Date']

# Convert each date to a nicely formatted string
formatted_dates = [date.strftime("%B %d, %Y") for date in earnings_dates]

# Print nicely formatted earnings dates
if len(formatted_dates) == 1:
print(f"Earnings date for {stock_symbol}: {formatted_dates[0]}")
else:
print(f"Earnings dates for {stock_symbol}: {' - '.join(formatted_dates)}")
else:
print(f"Earnings date not found for {stock_symbol}.")