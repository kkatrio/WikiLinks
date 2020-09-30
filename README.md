### WikiLinks

### [@WikiLinkedList](https://twitter.com/WikiLinkedList)

**WikiLinks** is a twitter bot that tweets wikipedia linked articles. Each article in a tweet is chosen randomly out of all the links of the last tweet.

### Basic architecture

It's running as a cron job every hour on a rasperry pi.

It's using [wikipedia-api](https://pypi.org/project/Wikipedia-API/) to parse wikipedia articles and [python-twitter](https://github.com/bear/python-twitter) to access the twitter API.

### Setup

This is done with python's virtualenv. Basic steps to install:
- `python -m pip install --user virtualenv`
- append /home/pi/.local/bin in PATH
- `virtualenv venv`
- source venv/bin/activate
- pip install python-twitter
- pip install wikipedia-api
- have credentials in a cred.json
```
{
    "consumer key": "",
    "consumer secret": "",
    "access token key": "",
    "access token secret": ""
}
```
Quick test if it works with:
- ./test_api.py
- ./test_scrapper.py

Run (and post) with:
- ./run.sh
