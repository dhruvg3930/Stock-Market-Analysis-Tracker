# Stock Market Analysis Tool

This Python project provides a comprehensive tool for analyzing historical stock market data. It includes functionalities for fetching historical data, calculating returns, volatility measures, 
plotting stock prices, moving averages, rolling volatilities, and visualizing the distribution of daily returns. The project utilizes the Yahoo Finance API through the `yfinance` library 
for data retrieval.

## Features

- **Fetching Historical Data**: Retrieve historical stock market data for a specified stock symbol and date range.
- **Calculating Returns**: Calculate daily returns based on adjusted closing prices.
- **Calculating Volatility**: Compute annualized volatility using the standard deviation of returns.
- **Plotting Stock Price**: Visualize the adjusted closing price of the stock over time.
- **Calculating Moving Average**: Compute the moving average of the stock's adjusted closing price.
- **Plotting Stock with Moving Average**: Visualize the stock's adjusted closing price along with its moving average.
- **Calculating Rolling Volatility**: Compute rolling volatility of the stock over a specified window.
- **Plotting Rolling Volatility**: Visualize the rolling volatility of the stock over time.
- **Additional Seaborn Plots**: Include an additional Seaborn plot to visualize the distribution of daily returns using a histogram.


## Usage

- Run the script `stock-market-analysis-tracker.py`
- When prompted, enter the stock symbol, start date, and end date.
- View the calculated statistics and plots generated.

## Requirements

This project requires the following libraries:

`yfinance` `pandas` `matplotlib` `seaborn`

These libraries can be installed using pip:

```bash
pip install yfinance pandas matplotlib seaborn

