import local_functions
from pathlib import Path
import json

# Update all scores for today
local_functions.getScores()

# Update all team files
local_functions.getTeams()

# Update all team rosters, player stats, and team schedules
## Iterate through teams file
with open("teams.json", 'r') as f:
    for line in f:
        team = json.loads(line)
        # Get team name 
        team_name = team['slug']
        # Get team links list
        team_links = team['links']
        team_roster_url = ''
        team_stats_url = ''
        team_schedule_url = ''
        # Iterate team links list to find roster, stats, and schedule urls
        for link in team_links:
            if link['text'] == 'Roster':
                team_roster_url = link['href']
            if link['text'] == 'Statistics':
                team_stats_url = link['href']
            if link['text'] == 'Schedule':
                team_schedule_url = link['href']
        # Call getPlayers to get updated team rosters
        local_functions.getPlayers(team_name, team_roster_url)
        # Call getPlayerStats to get updated team rosters
        local_functions.getPlayerStats(team_name, team_stats_url)
        # # Call getSchedule to get updated team schedule
        local_functions.getSchedule(team_name, team_schedule_url)