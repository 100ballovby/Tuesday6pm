import requests

url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv'
target_csv = 'nba_all_elo.csv'

response = requests.get(url)
response.raise_for_status()
with open(target_csv, 'wb') as f:
    f.write(response.content)
print('Downloaded!')