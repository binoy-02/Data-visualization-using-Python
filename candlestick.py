import pandas as pd
import mplfinance as mpf

# Sample data
data = {
    'Date': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05'],
    'Open': [100, 102, 104, 103, 105],
    'High': [105, 106, 108, 107, 109],
    'Low': [99, 101, 102, 101, 104],
    'Close': [104, 105, 107, 106, 108],
    'Volume': [1500, 1600, 1700, 1400, 1800]
}

# Convert to DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Plotting the candlestick chart
mpf.plot(df, type='candle', volume=True, title='Candlestick Chart Example', style='yahoo')
