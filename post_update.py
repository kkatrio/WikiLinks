import twitter
import json
import scrap_wikipedia


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

def get_last_link():
    statuses = api.GetUserTimeline(screen_name='bitonic5000')
    return scrap_wikipedia.retrieve_last_node(statuses)

# main
filename = 'cred.json'
with open(filename) as f:
    data = json.load(f)

api = twitter.Api(consumer_key=data['consumer key'],
                  consumer_secret=data['consumer secret'],
                  access_token_key=data['access token key'],
                  access_token_secret=data['access token secret'])

# get last tweet
last_page = get_last_link()
print(last_page)

# scrap article from last link
try:
    content = scrap_wikipedia.wiki_content(last_page)
    process_tweet(content)
except AssertionError:
    print("Can't scrap wiki page")
