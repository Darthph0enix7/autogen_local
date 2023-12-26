# Import necessary libraries
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Get the stock prices for AMZN, AAPL, and INTC
data = yf.download('AMZN', 'AAPL', 'INTC')['Close']

# Create a DataFrame with the data
df = pd.DataFrame(data, columns=['AMZN', 'AAPL', 'INTC'])

# Set the index to be the date
df.index = df.index.date

# Resample the data to yearly frequency
df_yearly = df.resample('1Y').sum()

# Plot the stock prices
plt.plot(df_yearly)
plt.xlabel('Year')
plt.ylabel('Stock Price ($)')
plt.title('Stock Prices for AMZN, AAPL, and INTC YTD')
plt.savefig('stock_price_ytd.png')

# Terminate the program
print("TERMINATE")