import twitter
import json
from scrap_wikipedia import Wiki_scrapper


def post_tweet():
    try:
        #status = api.PostUpdate(content)
        print('ok')
    except UnicodeDecodeError:
        print("Your message could not be encoded.  Perhaps it contains non-ASCII characters? ")
        print("Try explicitly specifying the encoding with the --encoding flag")
        sys.exit(2)
        print("{0} just posted: {1}".format(status.user.name, status.text))

def process_tweet(content):
    print(content)

def get_last_link(scrapper, api):
    statuses = api.GetUserTimeline(screen_name='bitonic5000')
    return scrapper.retrieve_last_node(statuses)


def main():
    # get twiter credentials
    filename = 'cred.json'
    with open(filename) as f:
        data = json.load(f)

    api = twitter.Api(consumer_key=data['consumer key'],
                      consumer_secret=data['consumer secret'],
                      access_token_key=data['access token key'],
                      access_token_secret=data['access token secret'])


    scrapper = Wiki_scrapper()


    # get last tweet
    last_page = get_last_link(scrapper, api)
    print(last_page)

    # scrap article from last link
    try:
        content = scrapper.wiki_content(last_page)
        process_tweet(content)
    except AssertionError:
        print("Can't scrap wiki page")


if __name__ == "__main__":
    main()
