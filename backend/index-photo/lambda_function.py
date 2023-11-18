import json
import os
import logging

import boto3
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

REGION = 'us-east-1'
SERVICE = 'es'
HOST = 'search-album-6ut2uyuvskblh5kaavysimss3i.aos.us-east-1.on.aws' #to change to cloud formation opensearch
PORT = 443
INDEX = 'album'
MAX_LABELS = 100


def lambda_handler(event, context):
    print('enter index-photos')
    print('received event: ' + json.dumps(event))
    bucket, object_key, created_timestamp, custom_label = s3(event)
    rekognition_labels = rekognition(bucket, object_key)
    labels = []
    labels.append(custom_label)
    labels.extend(rekognition_labels)
    open_search(object_key, bucket, created_timestamp, labels)


def s3(event):
    print("enter s3")
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    head_object = s3.head_object(Bucket=bucket, Key=object_key)
    print(f"head_object: {head_object}")
    custom_label = head_object["Metadata"]["customlabels"]
    created_timestamp = head_object["LastModified"].strftime("%Y-%m-%dT%H:%M:%S")

    return bucket, object_key, created_timestamp, custom_label


def rekognition(bucket, object_key):
    print("enter rekognition")
    rekognition = boto3.client('rekognition')
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket':bucket, 'Name':object_key}}, MaxLabels=MAX_LABELS
    )
    print(f"rekognition response: {response}")
    labels = [label['Name'] for label in response['Labels']]

    return labels


def open_search(object_key, bucket, created_timestamp, labels):
    print("enter open_search")
    object = {
        "objectKey": object_key,
        "bucket": bucket,
        "createdTimestamp": created_timestamp,
        "labels": labels
    }
    print(f"open_search object: {object}")

    open_search = OpenSearch(
        hosts=[{'host': HOST,'port': PORT}],
        http_auth=get_aws_auth(),
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )

    try:
        response = open_search.index(index=INDEX, id=object["objectKey"], body=json.dumps(object))
        print(f"open_search response: {response}")
        print(open_search.get(index=INDEX, id=object["objectKey"]))
        return response
    except Exception as e:
        print(f"failed to index photo: {e}")
        raise e


def get_aws_auth():
    credentials = boto3.Session().get_credentials()
    return AWS4Auth(credentials.access_key,
                    credentials.secret_key,
                    REGION,
                    SERVICE,
                    session_token=credentials.token)

