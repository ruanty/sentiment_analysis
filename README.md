# sentiment_analysis
How social sentiment influence stock / crypto market

### 📄 TODO List

#### Stage 1. Data Pulling

- [ ] ~~Twitter academic account~~ 
- [x] Implement data fetching function
- [ ] Implement `Crontab` function


### Documentation

* [fetch.py](https://github.com/summerzhang423/sentiment_analysis/blob/main/fetch.py): Main script for fetching the data.
* [fetch_util.py](https://github.com/summerzhang423/sentiment_analysis/blob/main/fetch_util.py): Implementations of the functions used in `fetch.py`.
* [data/](https://github.com/summerzhang423/sentiment_analysis/tree/main/data): Directory for data files.

### How to fetch the data?

```bash
$ python fetch.py 
Successful wrote 500 records.
```

### How to change the parameters for searching?

Modify the values of the following variables in `fetch.py`.

```python
keyword = "btc"
N = 500
isTimeRange = False
# The following time range must be given if `isTimeRange` is set to True
since = None
until = None
```

-------------
sentiment code reference: https://towardsdatascience.com/step-by-step-twitter-sentiment-analysis-in-python-d6f650ade58d

