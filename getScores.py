import functions_framework
from google.cloud import bigquery
from urllib.request import urlopen
from datetime import datetime
import json

# Writes/updates today's game scores to BigQuery
@functions_framework.http
def main(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    try:
        # Define the ESPN endpoint containing all NCAAB teams
        endpoint = "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard?limit=500"
        # Open the URL and read in the HTML
        page = urlopen(endpoint)
        # Load data from page
        data = json.loads(page.read().decode('utf-8'))
        # Get events content
        content = data['events']
        # Get events date and create datetime obj
        # date = data['day']['date']
        date = datetime.strptime(data['day']['date'], "%Y-%m-%d")
        # Convert date from YYYY-MM-DD to YYYYMMDD for table sharding
        shard_date = date.strftime("%Y%m%d")

       # Set table destination variables
        project_id = "ncaa-player-bracket"
        dataset_id = "scores"
        table_id = f"scores_{shard_date}"
        
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
        job = client.load_table_from_json(content, table, job_config = job_config)

        # Return job result
        result = job.result()
        return str(result)

    except Exception as e:
        print(f"An error occurred while retrieving game scores. Error: {e}")
        return e
