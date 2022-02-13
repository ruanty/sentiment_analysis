import os
import requests
import json
import datetime
import time
import boto3

# Diane
BEARER_TOKEN = 'ADD_YOURS'
SEARCH_QUERY = [ '%23StopAAPIhate', '%23StopAsianhate',  '%23IAmNotAVirus']

FROM_DATE = datetime.date(2020,1,1)
TO_DATE = datetime.date(2021,8,31)

GEO_FIELDS = 'expansions=geo.place_id&place.fields=contained_within,country,country_code,full_name,geo,id,name,place_type'
TWEET_FIELDS = 'tweet.fields=created_at,in_reply_to_user_id,public_metrics,entities,context_annotations,attachments,referenced_tweets,source'


MAX_RESULTS = 100 # Number of Tweets you want to collect per keyword per day (500 limits)

# Script prints an update to the CLI every time it collected another X Tweets
PRINT_AFTER_X = 100

RATE_LIMIT = 900 # based on the API, you can have 900 request/15 min
PAUSING_TIME = 20 # seconds 

BUCKET_NAME = 'usf-aapi'


def search_twitter(query, TWEET_FIELDS, GEO_FIELDS, bearer_token = BEARER_TOKEN):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}

    url = "https://api.twitter.com/2/tweets/search/all?query={}&{}&{}&max_results={}".format(
        query, TWEET_FIELDS, GEO_FIELDS, MAX_RESULTS
    )
    response = requests.request("GET", url, headers=headers)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


s3 = boto3.resource('s3')

for date in daterange(FROM_DATE, TO_DATE):
    for hr in range(0, 24):
        if(hr < 23):
            #filter = f"lang:en place_country:US&start_time={date}T{hr:02d}:00:00Z&end_time={date}T{hr+1:02d}:00:00Z"
            filter = f"lang:en&start_time={date}T{hr:02d}:00:00Z&end_time={date}T{hr+1:02d}:00:00Z"

        else:
            #filter = f"lang:en place_country:US&start_time={date}T{hr:02d}:00:00Z&end_time={date+ datetime.timedelta(days=1)}T00:00:00Z"
            filter = f"lang:en&start_time={date}T{hr:02d}:00:00Z&end_time={date+ datetime.timedelta(days=1)}T00:00:00Z"

        #print(filter)
        for key_word in SEARCH_QUERY:
            query = f"{date} {key_word} {filter}"
            result = search_twitter(query, TWEET_FIELDS , GEO_FIELDS, bearer_token = BEARER_TOKEN)
            print(f'---{result}')
            FILENAME = f'{key_word}/tweets_{date}T{hr:02d}_{key_word}.json'
            
            object = s3.Object(BUCKET_NAME, f'new_tweets_without_constraint/{FILENAME}')
            object.put(Body=(bytes(json.dumps(result).encode('UTF-8'))))
            
            time.sleep(PAUSING_TIME)
