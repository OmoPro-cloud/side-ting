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

#NUMPY TASKS

#Array Slicing: Load the numeric data (Age, Appearances, Goals, Assists) into a NumPy array. Use slicing to extract only Appearances and Goals columns.



#Goals–Assists Ratio: Compute the ratio Goals / Assists for each player. Identify which player has the highest value.



#Standardize Goals: Perform Z‑score normalization on the Goals array then, find which player’s normalized value is closest to zero (the mean).



#Percentile Filtering: Determine the top 20th percentile for Goals and Assists separately. Use Boolean masking to list which players fall above each threshold.




#Random Perturbation & Mean Difference: Create a small random noise array (e.g. ±5% of Goals) and add it to the Goals array. Compute and report the mean difference between the original and perturbed goals.




#PANDAS TASKS
#Efficient Column: Add a new DataFrame column called Goal_Efficiency = Goals / Appearances, and round it to two decimal places.
goal_efficiency = df['Goals' / 'Appearances']
goal_eff_rounded = round(goal_efficiency, 2)
print(goal_eff_rounded)



#Top Performers by Club: For each club, find the player(s) with the highest number of Goals. Present a summary table showing club and top scorer(s).




#Position-Based Averages: Group by Position and compute the average Age, Goals, and Assists for each position category.




#Filter & Sort: Extract all CF (Center Forwards), then sort them by descending Goals, showing only Name, Club, and Goals.




#Club-Wide Rankings: Within each club, rank players by Assists. Create a new column Assist_Rank reflecting this. Then, display each club's data sorted by rank.