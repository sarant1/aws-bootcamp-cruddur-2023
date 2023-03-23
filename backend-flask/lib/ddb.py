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
        print('query-param================================', flush=True)
        print(query_params, flush=True)
        print('client============================', flush=True)
        print(client, flush=True)

        # query the table
        response = client.query(**query_params)
        items = response['Items']
        print(items, flush=True)
        results = []

        for item in items:
            last_sent_at = item['sk']['S']
            results.append({
                'uuid': item['message_group_uuid']['S'],
                'display_name': item['user_display_name']['S'],
                'handle': item['user_handle']['S'],
                'message': item['message']['S'],
                'created_at': last_sent_at
            })
        return results