import json
import boto3
import pandas as pd
import requests
from io import StringIO

def lambda_handler(event, context):
    print('event ->', event)

    response = requests.get("https://amazon.com")
    print(response.text())

    bucket = event['Records'][0]['bucket']['name']
    key = event['Records'][0]['object']['key']

    s3_client = boto3.client('s3')
    s3_object = s3_client.get_object(Key=key, Bucket=bucket)
    file_content = s3_object['body'].read().decode('utf-8')

    data = file_content.readcsv(StringIO(file_content))
    print(data)