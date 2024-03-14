import yfinance as yf
import win32com.client

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
        
        # Iterate over each earnings date range and create events in Outlook calendar
        for earnings_date_range in earnings_dates:
            # If earnings_date_range is a single date, convert it to a list containing one date
            if not isinstance(earnings_date_range, list):
                earnings_date_range = [earnings_date_range]
                
            # Extract start and end dates from the range
            start_date, end_date = earnings_date_range
            
            # Create appointment item
            appointment = outlook.CreateItem(1)
            appointment.Subject = f"Earnings Date Range - {stock_symbol}"
            appointment.Start = start_date
            appointment.End = end_date  # Set the end date of the event
            appointment.Save()
            
            print(f"Event created for {stock_symbol} from {start_date} to {end_date}")
                
    else:
        print(f"Earnings date not found for {stock_symbol}.")