import pandas as pd

df = pd.read_csv('2019_prem_players_stats.csv')
print(df.head())

#print top 10 goals of dataframe
all_gs = df.groupby('goals_overall')['full_name'].max().reset_index()
top10_gs = df.sort_values('goals_overall', ascending=False).head(10)
print('\nTop 10 goals scorers this season: ')
print(top10_gs)

