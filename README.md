# WikiLinks

## [@WikiLinkedList](https://twitter.com/WikiLinkedList)

**WikiLinks** is a twitter bot that tweets wikipedia linked articles. Each article in a tweet is chosen randomly out of all the links of the last tweet.

### Basic architecture

It runs as a cron job every ten minutes.

It's using [wikipedia-api](https://pypi.org/project/Wikipedia-API/) to parse wikipedia articles and [python-twitter](https://github.com/bear/python-twitter) to access the twitter API.
