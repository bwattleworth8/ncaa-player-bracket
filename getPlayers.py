from google.cloud import bigquery
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re

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
            # Name matches expected format, add First Last to name_alt and number to number list
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

        # Set table destination variables
        project_id = "ncaa-player-bracket"
        dataset_id = "rosters"
        table_id = {team_name}
        
        # Create BQ client
        client = bigquery.Client(project = project_id)
        dataset = client.dataset(dataset_id)
        table = dataset.table(table_id)

        # Configure job
        job_config = bigquery.LoadJobConfig(
            source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
            autodetect = True
        )
        job = client.load_table_from_dataframe(
            roster_df, table, job_config=job_config
        )

        # Return job result
        result = job.result()
        return result

    except Exception as e:
        print(f"An error occurred while retrieving and writing roster for {team_name}. Error: {e}")
        return e