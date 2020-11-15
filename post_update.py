#!/usr/bin/env python
import os
import twitter
import json
from scrap_wikipedia import Wiki_scrapper


def post_tweet(content, api):
    try:
        status = api.PostUpdate(content)
        print('ok')
    except UnicodeDecodeError:
        print("Your message could not be encoded.  Perhaps it contains non-ASCII characters? ")
        print("Try explicitly specifying the encoding with the --encoding flag")
        sys.exit(2)
    print("{0} just posted: {1}".format(status.user.name, status.text))

def print_tweet(content):
    print(content)

def get_link(api, i):
    statuses = api.GetUserTimeline(screen_name='WikiLinkedList')

    # get the text of the last posted tweet
    last_status = statuses[i] # 0 = last, 1 = previous
    last_text = last_status.text
    title_text = last_text.split(' - https://')[0]
    return title_text

def main():
    # get twiter credentials
    filename = os.getcwd() + '/cred.json'
    with open(filename) as f:
        data = json.load(f)

    api = twitter.Api(consumer_key=data['consumer key'],
                      consumer_secret=data['consumer secret'],
                      access_token_key=data['access token key'],
                      access_token_secret=data['access token secret'])

    scrapper = Wiki_scrapper()

    # get last tweet
    last_page = get_link(api, 0) # try last first

    try:
        # scrap article from last link
        content = scrapper.wiki_content(last_page)
        if content is None:
            previous_page = get_link(api, 1) # previous
            scrapper.reset()
            content = scrapper.wiki_content(previous_page)
        # post new
        post_tweet(content, api)
    except AssertionError:
        print("Can't scrap wiki page")

if __name__ == "__main__":
    main()
