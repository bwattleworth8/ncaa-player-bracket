from google.cloud import bigquery
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# Writes a json file of per game stats and season total stats for players of given team
## Requires a team's ESPN team name and team stats URL
def getPlayerStats(team_name, team_stats_url):
    try:
        # Open the URL and read in the HTML
        page = urlopen(team_stats_url)

        # Decode the HTML
        html = page.read().decode("utf-8")
        
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        
        # Find the Per Game Stats table
        ## First get the players names
        per_game_stats_players = soup.findAll('table', {'class': 'Table Table--align-right Table--fixed Table--fixed-left'})[0]
        ## Then get their respective stats
        per_game_stats_metrics = soup.findAll('table', {'class': 'Table Table--align-right'})[0]
        
        # Find the Season Totals table
        ## First get the players names
        season_totals_players = soup.findAll('table', {'class': 'Table Table--align-right Table--fixed Table--fixed-left'})[1]
        ## Then get their respective stats
        season_totals_metrics = soup.findAll('table', {'class': 'Table Table--align-right'})[1]
        
        # Convert the stats tables to DataFrames
        per_game_stats_players_df = pd.read_html(str(per_game_stats_players))[0]
        per_game_stats_metrics_df = pd.read_html(str(per_game_stats_metrics))[0]
        season_totals_players_df = pd.read_html(str(season_totals_players))[0]
        season_totals_metrics_df = pd.read_html(str(season_totals_metrics))[0]
        
        # Concatenate the player and metric tables for both per game and season tables
        per_game_stats_df = pd.concat([per_game_stats_players_df, per_game_stats_metrics_df], axis=1)
        season_totals_df = pd.concat([season_totals_players_df, season_totals_metrics_df], axis=1)        
        
        # Set table destination variables
        project_id = "ncaa-player-bracket"
        dataset_id = "statistics"

        # Set table_ids for each df
        table_id1 = {team_name} + "_per_game"
        table_id2 = {team_name} + "_season"
        
        # Create BQ client
        client = bigquery.Client(project = project_id)
        dataset = client.dataset(dataset_id)
        table1 = dataset.table(table_id1)
        table2 = dataset.table(table_id2)

        # Configure job
        job_config = bigquery.LoadJobConfig(
            source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
            autodetect = True
        )
        job1 = client.load_table_from_dataframe(
            per_game_stats_df, table1, job_config=job_config
        )
        job2 = client.load_table_from_dataframe(
            season_totals_df, table2, job_config=job_config
        )

        # Return job results
        result1 = job1.result()
        result2 = job2.result()
        return f"Job 1 result: \n\n {result1} \n\n Job 2 result: \n\n {result2}"

    except Exception as e:
        print(f"An error occurred while retrieving player statistics for {team_name}. Error: {e}")
        return e