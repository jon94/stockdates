import yfinance as yf
import win32com.client
from datetime import datetime

# List of stocks to track
stocks = ["ADBE", "AAPL", "MSFT"]  # Example list of stocks

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
        
        # Create Outlook Application object
        outlook = win32com.client.Dispatch("Outlook.Application")
        namespace = outlook.GetNamespace("MAPI")
        calendar = namespace.GetDefaultFolder(9)  # 9 represents the Outlook Calendar
        
        # Iterate over each earnings date and create event in Outlook calendar
        for earnings_date in earnings_dates:
            # Create appointment item
            appointment = outlook.CreateItem(1)
            appointment.Subject = f"Earnings Date - {stock_symbol}"
            appointment.Start = earnings_date
            appointment.Duration = 60  # in minutes
            appointment.Save()
            print(f"Event created for {stock_symbol} on {earnings_date}")
    else:
        print(f"Earnings date not found for {stock_symbol}.")
