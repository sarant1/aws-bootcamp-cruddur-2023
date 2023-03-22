import os,sys
import boto3
from datetime import datetime, timedelta, timezone
import uuid

class Ddb:
    def client():
        endpoint_url = os.getenv("AWS_ENDPOINT_URL")
        if endpoint_url:
            attrs = { 'endpoint_url': endpoint_url }
        else:
            attrs = {}
        dynamodb = boto3.client('dynamodb',**attrs)
        return dynamodb
    def list_message_groups(client, my_user_uuid):
        current_year = datetime.now().year
        table_name = 'cruddur-message'
        query_params = {
            'TableName': table_name,
            'KeyConditionExpression': 'pk = :pk AND begins_with(sk,:year)',
            'ScanIndexForward': False,
            'Limit': 20,
            'ExpressionAttributeValues': {
                ':year': {'S': str(current_year) },
                ':pk': {'S': f"GRP#{my_user_uuid}"}
            }
        }