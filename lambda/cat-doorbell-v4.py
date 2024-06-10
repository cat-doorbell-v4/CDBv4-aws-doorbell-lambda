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
        # Get the HTTP method and path
        http_method = event['httpMethod']
        path = event['path']

        if http_method == 'POST' and path == '/ring':
            return handle_ring(event)
        elif http_method == 'POST' and path == '/heartbeat':
            return handle_heartbeat(event)
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


def handle_ring(event):
    try:
        message = json.loads(event['body'])
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


def handle_heartbeat(event):
    try:
        message = json.loads(event['body'])
        print(f"Heartbeat received: {message}")
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
