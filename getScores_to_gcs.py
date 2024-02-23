import functions_framework
from google.cloud import storage
from urllib.request import urlopen
from datetime import datetime
import json

# Writes/updates today's game scores to GCS
@functions_framework.http
def main(request):

    request_json = request.get_json(silent=True)
    request_args = request.args

    try:
        # Define the ESPN endpoint containing all NCAAB teams
        endpoint = "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard?limit=500"
        # Open the URL and read in the HTML
        page = urlopen(endpoint)
        # Load data from page
        data = json.loads(page.read().decode('utf-8'))
        # Get events content, convert List to json string
        content = json.dumps(data['events'])
 
        # Get timestamp
        run_time = str(datetime.now().strftime("%Y-%m-%dT%H%M%SZ"))

       # Set GCS destination path
        bucket_name = "ncaab-espn"
        file_path = f"score_updates/scores_{run_time}"
        
        # Instantiate client and upload file to blob
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_path)
        blob.upload_from_string(data=content, content_type="application/json")

        print(f"NCAAB scores updated at {run_time}.")
        return ("Success")
    except Exception as e:
        print(f"An error occurred while retrieving game scores. Error: {e}")
        return e
