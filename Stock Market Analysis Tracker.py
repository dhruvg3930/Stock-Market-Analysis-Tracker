import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def fetch_stock_data(stock_symbol, start_date, end_date):
    """
    Fetching historical stock market data using yfinance.
    
    Parameters:
    stock_symbol (str): Ticker symbol of the stock.
    start_date (str): Start date for historical data in 'YYYY-MM-DD' format.
    end_date (str): End date for historical data in 'YYYY-MM-DD' format.
    
    Returns:
    pandas.DataFrame: Historical stock market data.
    """
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    return stock_data

def calculate_returns(stock_data):
    """
    Calculating daily returns of the stock.
    
    Parameters:
    stock_data (pandas.DataFrame): Historical stock market data.
    
    Returns:
    pandas.Series: Daily returns of the stock.
    """
    daily_returns = stock_data['Adj Close'].pct_change().dropna()
    return daily_returns

def calculate_volatility(returns):
    """
    Calculating annualized volatility of the stock.
    
    Parameters:
    returns (pandas.Series): Daily returns of the stock.
    
    Returns:
    float: Annualized volatility.
    """
    volatility = returns.std() * (252 ** 0.5)
    return volatility

def plot_stock_price(stock_data):
    """
    Ploting the adjusted closing price of the stock.
    
    Parameters:
    stock_data (pandas.DataFrame): Historical stock market data.
    """
    plt.figure(figsize=(10, 6))
    stock_data['Adj Close'].plot()
    plt.title('Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.show()

def calculate_moving_average(stock_data, window=20):
    """
    Calculating the moving average of the stock's adjusted closing price.
    
    Parameters:
    stock_data (pandas.DataFrame): Historical stock market data.
    window (int): Window size for the moving average calculation.
    
    Returns:
    pandas.Series: Moving average of the stock's adjusted closing price.
    """
    moving_avg = stock_data['Adj Close'].rolling(window=window).mean()
    return moving_avg

def plot_stock_with_moving_average(stock_data, moving_avg, window):
    """
    Ploting the stock's adjusted closing price along with the moving average.
    
    Parameters:
    stock_data (pandas.DataFrame): Historical stock market data.
    moving_avg (pandas.Series): Moving average of the stock's adjusted closing price.
    window (int): Window size for the moving average calculation.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['Adj Close'], label='Adjusted Close')
    plt.plot(moving_avg.index, moving_avg, label=f'{window}-Day Moving Average')
    plt.title('Stock Price with Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

def calculate_rolling_volatility(stock_data, window=20):
    """
    Calculating rolling volatility of the stock.
    
    Parameters:
    stock_data (pandas.DataFrame): Historical stock market data.
    window (int): Window size for the rolling volatility calculation.
    
    Returns:
    pandas.Series: Rolling volatility of the stock.
    """
    rolling_volatility = stock_data['Adj Close'].pct_change().rolling(window=window).std() * (252 ** 0.5)
    return rolling_volatility

def plot_rolling_volatility(rolling_volatility):
    """
    Ploting rolling volatility of the stock.
    
    Parameters:
    rolling_volatility (pandas.Series): Rolling volatility of the stock.
    """
    plt.figure(figsize=(10, 6))
    rolling_volatility.plot()
    plt.title('Rolling Volatility')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.grid(True)
    plt.show()

def main():
    stock_symbol = input("Enter the stock symbol (e.g., AAPL): ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    # Fetch historical stock market data
    stock_data = fetch_stock_data(stock_symbol, start_date, end_date)

    # Calculate and print basic statistics
    returns = calculate_returns(stock_data)
    volatility = calculate_volatility(returns)
    print(f"Annualized Volatility: {volatility:.2f}")

    # Plot stock price
    plot_stock_price(stock_data)

    # Calculating and plot moving average
    window = 20  # You can change the window size as needed
    moving_avg = calculate_moving_average(stock_data, window)
    plot_stock_with_moving_average(stock_data, moving_avg, window)

    # Calculating and plot rolling volatility
    rolling_volatility = calculate_rolling_volatility(stock_data, window)
    plot_rolling_volatility(rolling_volatility)

    # Additional Seaborn plots
    plt.figure(figsize=(10, 6))
    sns.histplot(returns, bins=30, kde=True)
    plt.title('Distribution of Daily Returns')
    plt.xlabel('Daily Returns')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
