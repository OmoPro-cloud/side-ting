import pandas as pd

df = pd.read_csv('footballers.csv')
print(df)
print('-' * 30)

#display shape and columns of dataframe
print(df.shape)
print(df.columns)

#Filter through data
#print people whose age is greater than 25
print(df[df['Age'] > 25])

#print people who;s age is greater than 20 and plays for arsenal
print(df[df['Age'] > 25])

#people whose age is greater than 25 and live in new york
#print(df1[(df1['Age'] > 25) & (df1['City'] == 'Chicago')])