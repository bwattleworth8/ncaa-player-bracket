from google.cloud import bigquery
from urllib.request import urlopen
import json

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
        
        # Set table destination variables
        project_id = "ncaa-player-bracket"
        dataset_id = "teams"
        table_id = "teams"
        
        # Create BQ client
        client = bigquery.Client(project = project_id)
        dataset = client.dataset(dataset_id)
        table = dataset.table(table_id)

        # Configure job
        job_config = bigquery.LoadJobConfig(
            source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
            autodetect = True
        )

        # Configure job
        job = client.load_table_from_json(data_nl, table, job_config = job_config)

        # Return job result
        result = job.result()
        return result
    
    except Exception as e:
        print(f"An error occurred while retrieving team data. Error: {e}")
        return e