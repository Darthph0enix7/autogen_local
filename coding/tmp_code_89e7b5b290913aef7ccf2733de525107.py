import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Get historical stock prices for AMZN, AAPL, and INTC
amzn = yf.download('AMZN', start='2019-01-01', end='2022-03-31')
aapl = yf.download('AAPL', start='2019-01-01', end='2022-03-31')
intc = yf.download('INTC', start='2019-01-01', end='2022-03-31')

# Create a DataFrame with the stock prices for each company
df = pd.concat([amzn, aapl, intc], axis=1)

# Plot the stock price change YTD for each company
ax1 = df['AMZN'].pct_change().plot(kind='bar', figsize=(15, 6))
ax2 = df['AAPL'].pct_change().plot(kind='bar', ax=ax1)
ax3 = df['INTC'].pct_change().plot(kind='bar', ax=ax1)

# Add a title and labels to the plot
plt.title('Stock Price Change YTD')
plt.xlabel('Date')
plt.ylabel('Percentage Change')

# Save the plot to a file
plt.savefig('stock_price_ytd.png')