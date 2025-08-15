import pandas as pd

df = pd.read_csv('footballers.csv')
print(df)
print('-' * 30)

#print whoever has more than 50 goals
print(df[df['Goals'] > 50]) 
print('-' * 30)

#print whoever has more than 80 assists
print(df[df['Assists'] > 80])
print('-' * 30)

#print whoever has more than 300 appearances
print(df[df['Appearances'] > 300])
print('-' * 30)