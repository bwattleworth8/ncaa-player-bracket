import functions_framework
from google.cloud import bigquery
from datetime import datetime
import os
import re

# Writes file to BQ when posted to GCS ncaab-espn
@functions_framework.cloud_event
def write_gcs_to_bq(cloud_event):
    
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    # GCS file upload metadata
    bucket = data["bucket"]
    file_name = data["name"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    date = datetime.now().date().strftime('%Y%m%d')

    table_id = f"ncaa-player-bracket.scores.scores_{date}"
    
    print(file_name) 

    #Create bq client
    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(
      autodetect=True,
      source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    )

    #Set URI for file locations
    uri = f'gs://{bucket}/{file_name}'

    load_job = client.load_table_from_uri(
        uri,
        table_id,
        location = "US",
        job_config = job_config
    )

    load_job.result()

    destination_table = client.get_table(table_id)
    print(f"Success. Shopify file uploaded to BigQuery, table id: {table_id}.")
