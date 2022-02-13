from fetch_util import *
from credential_pool import keys


def main():
    keyword = "btc"
    N = 500
    isTimeRange = False
    # The following time range must be given if `isTimeRange` is set to True
    since = None
    until = None

    for consumerKey, consumerSecret, accessToken, accessTokenSecret in keys:
        api = get_api(consumerKey, consumerSecret, accessToken, accessTokenSecret)
        if isTimeRange:
            tweets = get_data_range(api, keyword, since, until, N)
        else:
            tweets = get_data(api, keyword, N)
        save_df(tweets)


if __name__ == '__main__':
    main()