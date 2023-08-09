import requests
from collections import defaultdict
import pandas as pd


#Step 1: Extraction

# Fetch NBA team data
teams_url = 'https://www.balldontlie.io/api/v1/teams'
response = requests.get(teams_url)
teams_data = response.json()

# Fetch NBA player data
players_url = 'https://www.balldontlie.io/api/v1/players'
response = requests.get(players_url)
players_data = response.json()

#Step 2: Transformation

# Calculate total combined weight of each NBA team
team_weights = defaultdict(int)

for player in players_data['data']:
    team_id = player['team']['id']
    weight = player['weight_pounds']
    if weight is not None:  # Check if weight value exists
        team_weights[team_id] += weight

# Convert the transformed data to a DataFrame
team_weights_df = pd.DataFrame(list(team_weights.items()), columns=['Team ID', 'Total Weight'])

#Step 3: Loading
# Find the heaviest and lightest NBA teams
heaviest_team = team_weights_df.loc[team_weights_df['Total Weight'].idxmax()]
lightest_team = team_weights_df.loc[team_weights_df['Total Weight'].idxmin()]

print("Heaviest Team:")
print(heaviest_team)

print("\nLightest Team:")
print(lightest_team)

