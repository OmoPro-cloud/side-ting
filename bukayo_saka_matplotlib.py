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

#fig, ax = plt.subplots()
#ax.plot(df['Year'], df['G+A'], marker='o', linewidth=2)
#ax.set(title='Bukayo Saka G+A in all seasons', xlabel='Year', ylabel='G+A')
#ax.grid(True, alpha=0.5)
#plt.show()


#all_stats = df.groupby('Year')['G+A'].max().reset_index()
#overall_ga = all_stats.sort_values('G+A', ascending=False).head(5)
#print('\nTop 5 Highest G+As recorded: ')
#print(overall_ga)

avg_ga = df['G+A'].mean()
print('\n average g/a', avg_ga)