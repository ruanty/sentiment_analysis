import tweepy
import pandas as pd
from datetime import datetime


def get_api(consumerKey, consumerSecret, accessToken, accessTokenSecret):
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)
    return api


def get_data(api, keyword, noOfTweet) -> pd.DataFrame:

    tweet_df = pd.DataFrame()

    tweet_id = []
    tweet_list = []
    tweet_time = []
    tweet_user = []
    tweet_followers = []
    tweet_loc = []

    tweets = tweepy.Cursor(api.search_tweets,
                           q=keyword + " -filter:retweets -filter:replies",       # Filter retweets and replies
                           lang="en").items(noOfTweet)

    for tweet in tweets:
        tweet_id.append(tweet.id)
        tweet_list.append(tweet.text)
        tweet_time.append(tweet.created_at)
        tweet_user.append(tweet.user.name)
        tweet_followers.append(tweet.user.followers_count)
        tweet_loc.append(tweet.user.location)

    tweet_df["id"] = tweet_id
    tweet_df["username"] = tweet_user
    tweet_df["text"] = tweet_list
    tweet_df["create_time"] = tweet_time
    tweet_df["follower_count"] = tweet_followers
    tweet_df["location"] = tweet_loc

    return tweet_df


def get_data_range(api, keyword, since, until, noOfTweet) -> pd.DataFrame:

    tweet_df = pd.DataFrame()

    tweet_id = []
    tweet_list = []
    tweet_time = []
    tweet_user = []
    tweet_followers = []
    tweet_loc = []

    tweets = tweepy.Cursor(api.search_tweets,
                           q=keyword + " -filter:retweets -filter:replies",       # Filter retweets and replies
                           since=since,
                           until=until,
                           lang="en").items(noOfTweet)

    for tweet in tweets:
        tweet_id.append(tweet.id)
        tweet_list.append(tweet.text)
        tweet_time.append(tweet.created_at)
        tweet_user.append(tweet.user.name)
        tweet_followers.append(tweet.user.followers_count)
        tweet_loc.append(tweet.user.location)

    tweet_df["id"] = tweet_id
    tweet_df["username"] = tweet_user
    tweet_df["text"] = tweet_list
    tweet_df["create_time"] = tweet_time
    tweet_df["follower_count"] = tweet_followers
    tweet_df["location"] = tweet_loc

    return tweet_df


def save_df(df) -> None:
    timestamp = str(datetime.now()).replace(" ", "").replace("-", "").replace(":", "").replace(".", "")
    df.to_csv("./data/" + timestamp + ".csv", index=None)
    print("Successfully wrote 500 records.")

