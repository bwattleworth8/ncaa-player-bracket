from espnFunctions import *
import os, os.path

teams_endpoint = "https://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/teams/?group=50&limit=1000"

## Update teams file
# result = getTeams(teams_endpoint)
# print(result)

# # Read teams file
# f = open("teams.json", "r")
# teams = json.load(f)
# f.close()

# # Loop through teams in teams file
# for team in teams:
#     team_name = team['slug']
#     for link in team['links']:
#         if link['text'] == 'Roster':
#             # Update roster file for team
#             getRoster(team_name, link['href'])

# Loop through athletes
directory = 'rosters'
count = 0
getPlayers(url)
stats_url = f'http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2024/types/0/athletes/{id}/statistics/0'
getPlayerStats(id, stats_url)
