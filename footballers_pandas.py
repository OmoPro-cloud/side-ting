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

#Efficient Column: Add a new DataFrame column called Goal_Efficiency = Goals / Appearances, and round it to two decimal places.
goal_efficiency = df['Goals' / 'Appearances']
goal_eff_rounded = round(goal_efficiency, 2)
print(goal_eff_rounded)



#Top Performers by Club: For each club, find the player(s) with the highest number of Goals. Present a summary table showing club and top scorer(s).




#Position-Based Averages: Group by Position and compute the average Age, Goals, and Assists for each position category.




#Filter & Sort: Extract all CF (Center Forwards), then sort them by descending Goals, showing only Name, Club, and Goals.




#Club-Wide Rankings: Within each club, rank players by Assists. Create a new column Assist_Rank reflecting this. Then, display each club's data sorted by rank.