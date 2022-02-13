from fetch_util import *
from credential_pool import keys


def main():
    for consumerKey, consumerSecret, accessToken, accessTokenSecret in keys:
        api = get_api(consumerKey, consumerSecret, accessToken, accessTokenSecret)
        tweets = get_data(api, "btc", 500)
        save_df(tweets)


if __name__ == '__main__':
    main()