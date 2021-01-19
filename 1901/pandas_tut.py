import pandas as pd

nba = pd.read_csv('nba_all_elo.csv')

print(type(nba))
print(len(nba))
print(nba.shape)
print(nba.info())
print()
print(nba.describe())
print()
print(nba['fran_id'].value_counts())
print(nba.loc[nba['fran_id'] == 'Lakers', 'date_game'].agg(('min', 'max')))