# sentiment_analysis
How social sentiment influence stock / crypto market

### 📄 TODO List

#### Stage 1. Data Pulling

- [ ] ~~Twitter academic account~~ 
- [x] Implement data fetching function
  - `fetch.py` can only be used to retrieve CSV files, which may not be suitable for MongoDB.
  - `retrieve_tweets_with_details.py` can be used to pull JSON data but requires modification.
- [ ] Implement `Crontab` function


### 🗃 Documentation

* [social_sentiment_analysis.ipynb](https://github.com/summerzhang423/sentiment_analysis/blob/main/social_sentiment_analysis.ipynb): Initial testing.
* [fetch.py](https://github.com/summerzhang423/sentiment_analysis/blob/main/fetch.py): Main script for fetching the data.
* [fetch_util.py](https://github.com/summerzhang423/sentiment_analysis/blob/main/fetch_util.py): Implementations of the functions used in `fetch.py`.
* [data/](https://github.com/summerzhang423/sentiment_analysis/tree/main/data): Directory for data files.
* [retrieve_tweets_with_details.py](https://github.com/summerzhang423/sentiment_analysis/blob/main/retrieve_tweets_with_details.py): Diane's script for pulling JSON data.

### 🚀 FAQ for `fetch.py`

#### How to fetch the data?

```bash
$ python fetch.py 
Successful wrote 500 records.
```

#### How to change the parameters for searching?

Modify the values of the following variables in `fetch.py`.

```python
keyword = "btc"
N = 500
isTimeRange = False
# The following time range must be given if `isTimeRange` is set to True
since = None
until = None
```

#### Why there's no `credential_pool` module?

I chose to ignore this script because it is not smart to include secret keys in a public repo. So feel free to ask me for that or create your own `credential_pool` if you need.

-------------
sentiment code reference: https://towardsdatascience.com/step-by-step-twitter-sentiment-analysis-in-python-d6f650ade58d

