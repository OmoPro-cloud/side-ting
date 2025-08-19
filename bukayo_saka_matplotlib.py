import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bukayo_saka.csv')
print(df)

'''
fig, ax = plt.subplots()
ax.plot(df['Year'], df['Value'], marker='o', linewidth=0.5)
ax.set(title='time series demo', xlabel = 'Year', ylabel = 'Value')
ax.grid(True, alpha = 0.5)
plt.show()
'''