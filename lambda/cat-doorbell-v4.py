import json
import os

import boto3

# Initialize boto3 client for SNS
sns_client = boto3.client('sns')

# Environment variables
SNS_TOPIC_ARN = os.getenv('SNS_TOPIC_ARN')


def lambda_handler(event, context):
    print(f"Received event: {event}")
    try:
        http_method = event['httpMethod']
        path = event['path']
        device_quoted = event['body']
        device = device_quoted.replace('"', '')

        if http_method == 'POST' and path == '/ring':
            return handle_ring(device)
        elif http_method == 'POST' and path == '/heartbeat':
            return handle_heartbeat(device)
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Not Found'})
            }
    except Exception as e:
        print(f"Error processing request: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal Server Error'})
        }


def handle_ring(hostname):
    try:
        print(f"CDBv4-001I {hostname} ring received")
        message = f"{hostname} is ringing"
        sns_response = sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=json.dumps({'default': json.dumps(message)}),
            MessageStructure='json'
        )
        print(f"SNS response: {sns_response}")
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'SNS message sent successfully'})
        }
    except Exception as e:
        print(f"Error sending SNS message: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Failed to send SNS message'})
        }


def handle_heartbeat(hostname):
    try:
        print(f"CDBv4-002I {hostname} heartbeat received")
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Heartbeat logged successfully'})
        }
    except Exception as e:
        print(f"Error logging heartbeat: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Failed to log heartbeat'})
        }
