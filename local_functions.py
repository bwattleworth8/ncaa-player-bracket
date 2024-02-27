from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import re

import ssl

# Writes a json file of metadata for each NCAA men's basketball team into the teams/ directory
def getTeams():
    try:
        # Define the ESPN endpoint containing all NCAAB teams
        endpoint = "http://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/teams?limit=500"
        # Open the URL and read in the HTML
        page = urlopen(endpoint)
        # Decode the HTML to reveal standard json
        data = json.loads(page.read().decode('utf-8'))
        # Parse json data and isolate the teams list -- this is a list of dicts
        teams = data['sports'][0]['leagues'][0]['teams']
        # Prep data for write to file
        # Convert json to newline delimited json for BigQuery ingestion
        data_nl = '\n'.join([json.dumps(team['team']) for team in teams])
        # Set filename
        file_name = "teams.json"
        # Write to files
        f = open(file_name, "w")
        f.write(data_nl)
        f.close()
        string = f"Successfully wrote teams to teams file."
        return string
    except Exception as e:
        print(f"An error occurred while retrieving team data. Error: {e}")
        return e
    
# Writes a json file representing roster of given team into the rosters/ directory
## Requires a team's ESPN team name and roster URL
def getPlayers(team_name, team_roster_url):
    try:
        # Open the URL and read in the HTML
        page = urlopen(team_roster_url)
        # Decode the HTML
        html = page.read().decode("utf-8")
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        # Find the roster table
        roster = soup.find('table', {'class': 'Table'})
        # Individually, find the headshot images in the roster table
        img_elements = roster.find_all('img', {'alt': True})
        img_urls = []
        # Iterate through each img tag and add the alt attribute value to the img_urls list, contains headshot URL
        for img in img_elements:
            img_urls.append(img['alt'])
        # Convert the roster table to Pandas DataFrame
        roster_df = pd.read_html(str(roster))[0]
        # Drop the first column of DataFrame that contains NaNs for images
        roster_df.drop(columns=roster_df.columns[0], axis=1,  inplace=True)
        # Add a new Headshot column containing the player images
        roster_df.insert(0, "Headshot", img_urls, True)
        # Create Lists to hold new name and number columns
        name_alt = []
        number = []
        # Remove the player number from the name column and put it into its own column
        for index, row in roster_df.iterrows():
            # Looking for name format of First Last##, First and Last can be any non-numeric character
            name_number_format = re.search(r"([^0-9]+) ([^0-9]+)(\d+)?", row['Name'])
            if name_number_format:
                name_alt.append(name_number_format.group(1) + " " + name_number_format.group(2))
                number.append(name_number_format.group(3))
            else:
                raise Exception("At least one player name did not match expected name number format.")
        # Drop the old name column
        roster_df.drop(columns=roster_df.columns[1], axis=1,  inplace=True)
        # Insert updated name column and number column
        roster_df.insert(1, "Name", name_alt, True)
        roster_df.insert(2, "Number", number, False)
        # Set file_name and convert DataFrame to newline json, write to file
        file_name = f"rosters/{team_name}.json"
        data_nl = roster_df.to_json(file_name, orient="records", lines=True)
        return f"Successfully wrote roster for {team_name}."
    except Exception as e:
        print(f"An error occurred while retrieving and writing roster for {team_name}. Error: {e}")
        return e

# Writes a json file of per game stats and season total stats for players of given team
# Requires a team's ESPN team name and team stats URL
# def getPlayerStats(team_name, team_stats_url):
#     try:
#         # Open the URL and read in the HTML
#         page = urlopen(team_stats_url)
#         # Decode the HTML
#         html = page.read().decode("utf-8")
#         # Parse HTML with BeautifulSoup
#         soup = BeautifulSoup(html, "html.parser")
#         # Find the Per Game Stats table
#         ## First get the players names
#         per_game_stats_players = soup.findAll('table', {'class': 'Table Table--align-right Table--fixed Table--fixed-left'})[0]
#         ## Then get their respective stats
#         per_game_stats_metrics = soup.findAll('table', {'class': 'Table Table--align-right'})[0]
#         # Find the Season Totals table
#         ## First get the players names
#         season_totals_players = soup.findAll('table', {'class': 'Table Table--align-right Table--fixed Table--fixed-left'})[1]
#         ## Then get their respective stats
#         season_totals_metrics = soup.findAll('table', {'class': 'Table Table--align-right'})[1]
#         # Convert the stats tables to DataFrames
#         per_game_stats_players_df = pd.read_html(str(per_game_stats_players))[0]
#         per_game_stats_metrics_df = pd.read_html(str(per_game_stats_metrics))[0]
#         season_totals_players_df = pd.read_html(str(season_totals_players))[0]
#         season_totals_metrics_df = pd.read_html(str(season_totals_metrics))[0]
#         # Concatenate the player and metric tables for both per game and season tables
#         per_game_stats_df = pd.concat([per_game_stats_players_df, per_game_stats_metrics_df], axis=1)
#         season_totals_df = pd.concat([season_totals_players_df, season_totals_metrics_df], axis=1)        
#         # Set file_name and convert DataFrame to newline json, write to file
#         per_game_file_name = f"playerStats/{team_name}_per_game_stats.json"
#         season_file_name = f"playerStats/{team_name}_season_total_stats.json"
#         per_game_data = per_game_stats_df.to_json(per_game_file_name, orient='records', lines=True)
#         season_data = season_totals_df.to_json(season_file_name, orient='records', lines=True)
#         return f"Successfully wrote player stats files for {team_name}."
#     except Exception as e:
#         print(f"An error occurred while retrieving player statistics for {team_name}. Error: {e}")
#         return e

def getPlayerStats():
    try:
        playerStatsUrl = "https://www.espn.com/mens-college-basketball/stats/player"

        # Open the URL and read in the HTML
        response = requests.get(playerStatsUrl, verify=False)
        print(response)
        # Decode the HTML
        html = response.read().decode("utf-8")
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        # Find the player stats table
        player_stat_table = soup.find('table', {'class': 'ResponsiveTable'})

        player_start_pd = pd.read_html(str(player_stat_table))
        print(player_start_pd)

        # table_len = x
        # listX = []

        # for (x = 0 < table_len, x++):
        #     querySelectAll("rowClass")[x]







        # per_game_stats_players_df = pd.read_html(str(per_game_stats_players))[0]
        # per_game_stats_metrics_df = pd.read_html(str(per_game_stats_metrics))[0]
        # season_totals_players_df = pd.read_html(str(season_totals_players))[0]
        # season_totals_metrics_df = pd.read_html(str(season_totals_metrics))[0]
        # # Concatenate the player and metric tables for both per game and season tables
        # per_game_stats_df = pd.concat([per_game_stats_players_df, per_game_stats_metrics_df], axis=1)
        # season_totals_df = pd.concat([season_totals_players_df, season_totals_metrics_df], axis=1)        
        # # Set file_name and convert DataFrame to newline json, write to file
        # per_game_file_name = f"playerStats/{team_name}_per_game_stats.json"
        # season_file_name = f"playerStats/{team_name}_season_total_stats.json"
        # per_game_data = per_game_stats_df.to_json(per_game_file_name, orient='records', lines=True)
        # season_data = season_totals_df.to_json(season_file_name, orient='records', lines=True)
        return f"Successfully wrote player stat files."
    except Exception as e:
        print(f"An error occurred while retrieving player statistics. Error: {e}")
        return e
    
# Writes a json file representing the schedule of given team
## Requires a team's ESPN team name and scheudle URL
def getSchedule(team_name, team_schedule_url):
    try:
        # Open the URL and read in the HTML
        page = urlopen(team_schedule_url)
        # Decode the HTML
        html = page.read().decode("utf-8")
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        # Find the schedule table
        regular_season = soup.findAll('table', {'class': 'Table'})[0]
        # Convert table to DataFrame
        regular_season_df = pd.read_html(str(regular_season))[0]
        # Rename the columns
        regular_season_df = regular_season_df.rename({0: 'Date', 1: 'Opponent', 2: 'Result', 3: 'W-L (Conf)', 4: 'High Pts', 5: 'High Reb', 6: 'High Ast'}, axis="columns")
        # Drop column index 7, as it is empty
        regular_season_df = regular_season_df.drop([7], axis="columns")
        # Drop first two rows (and separator row for upcoming games if applicable) and reset index to clean up table
        regular_season_df = regular_season_df.drop(labels=[0, 1], axis=0).reset_index(drop=True)
        for index, row in regular_season_df.iterrows():
            if(row['Date'] == "DATE"):
                regular_season_df = regular_season_df.drop(labels=[index], axis=0).reset_index(drop=True)
        # Set file_name and convert DataFrame to newline json, write to file    
        file_name = f"schedules/{team_name}.json"
        data = regular_season_df.to_json(file_name, orient='records', lines=True)
        return f"Successfully wrote team schedule file for {team_name}."
    except Exception as e:
        print(f"An error occurred while retrieving and writing schedule for {team_name}. Error: {e}")
        return e

# Writes a json file of game scores for current date
def getScores():
    try:
        # Define the ESPN endpoint containing all NCAAB teams
        endpoint = "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard?limit=500"
        # Open the URL and read in the HTML
        page = urlopen(endpoint)
        # Load data from page
        data = json.loads(page.read().decode('utf-8'))
        # Get events
        events = data['events']
        #Get events date
        date = data['day']['date']
        # Prep data for write to file
        ## Convert json to newline delimited json for BigQuery ingestion
        data_nl = '\n'.join([json.dumps(record) for record in events])
        # Set filename, point to schedules/ directory
        file_name = f"games/{date}.json"
        # Write to file
        f = open(file_name, "w")
        f.write(data_nl)
        f.close()
        string = f"Successfully wrote today's games to the games/ directory."
        return string
    except Exception as e:
        print(f"An error occurred while retrieving game scores. Error: {e}")
        return e