import json
import boto3
import requests
from requests_aws4auth import AWS4Auth
from opensearchpy import OpenSearch, RequestsHttpConnection


REGION = 'us-east-1'
SERVICE = 'es'

HOST = 'search-album-6ut2uyuvskblh5kaavysimss3i.aos.us-east-1.on.aws' #to change to cloud formation opensearch
S3_URL = 'https://hw2-intelligent-photo-album.s3.amazonaws.com/' #to change cloud formation S3 photo bucket
PORT = 443
INDEX = 'album'
BOT_ID = 'L4DXTDFTQU'
ALIAS_ID = 'AUMMMGBSRD'
LOCAL_ID = 'en_US'
SESSION_ID = 'testuser'
SINGULARIZE_MAPPING = [
    ('people', 'person'),
    ('men', 'man'),
    ('wives', 'wife'),
    ('menus', 'menu'),
    ('us', 'us'),
    ('ss', 'ss'),
    ('is', 'is'),
    ("'s", "'s"),
    ('ies', 'y'),
    ('ies', 'y'),
    ('es', 'e'),
    ('s', '')
]


def lambda_handler(event, context):
    print('enter search-photos')
    print('received event: ' + json.dumps(event))

    labels = lex(event)
    open_search_response = open_search(labels)
    results = s3(open_search_response)

    return {
        'statusCode': 200,
        'headers':{
            'Access-Control-Allow-Origin':'*',
            'Access-Control-Allow-Credentials':True,
            'Access-Control-Request-Headers':'*',
            'Access-Control-Allow-Headers':'*'
        },
        'body': json.dumps({"results":results})
    }


def lex(event):
    print("enter lex")
    lex = boto3.client('lexv2-runtime')
    input_query = event['queryStringParameters']['q']
    print(f"input_query = {input_query}")
    input_query = input_query.lower()
    lex_response = lex.recognize_text(
            botId=BOT_ID, # MODIFY HERE
            botAliasId=ALIAS_ID, # MODIFY HERE
            localeId=LOCAL_ID,
            sessionId=SESSION_ID,
            text=input_query)

    print(f"lex_response = {lex_response}")

    labels = []
    intent = lex_response["sessionState"]["intent"]
    if intent["name"] == "SearchIntent":
        if intent['slots']['label1'] is not None:
            label_1 = intent['slots']['label1']["value"]["interpretedValue"]
            labels.append(singularize(label_1))
        if intent['slots']['label2'] is not None:
            label_2 = intent['slots']['label2']["value"]["interpretedValue"]
            labels.append(singularize(label_2))
    print(f"labels = {labels}")

    return labels


def open_search(labels):
    print("enter open_search")

    open_search = OpenSearch(
        hosts=[{'host': HOST,'port': PORT}],
        http_auth=get_aws_auth(),
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )
    response = []
    for label in labels:
        try:
            res = open_search.search(index=INDEX, body={"query":{"match":{"labels":label}}})
            response.append(res)
        except Exception as e:
            print(f"failed to search photo: {e}")
            raise e
    print(f"open_search response: {response}")

    return response


def s3(open_search_response):
    print("enter s3")
    s3 = boto3.client("s3")
    photos = {}
    for res in open_search_response:
        for hit in res['hits']['hits']:
            key = hit['_source']['objectKey']
            labels = hit['_source']['labels']
            if key not in photos:
                photos[key] = labels

    print(f"photos = {photos}")

    photos_result = []
    for key in photos.keys():
        info = {}
        # info["url"] = S3_URL + key
        info["url"] = s3.generate_presigned_url(ClientMethod="get_object", Params={"Bucket":"hw2-intelligent-photo-album", "Key":key}, ExpiresIn=3600)
        info["labels"] = photos[key]
        photos_result.append(info)

    print(f"photos_result = {photos_result}")

    return photos_result


def get_aws_auth():
    credentials = boto3.Session().get_credentials()
    return AWS4Auth(credentials.access_key,
                    credentials.secret_key,
                    REGION,
                    SERVICE,
                    session_token=credentials.token)


def singularize(noun):
    for plural, singular in SINGULARIZE_MAPPING:
        if noun.endswith(plural):
            return noun[:-len(plural)] + singular

    return noun