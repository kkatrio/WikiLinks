import twitter
import json
import scrap_wikipedia

'''
filename = 'cred.json'
with open(filename) as f:
    data = json.load(f)

api = twitter.Api(consumer_key=data['consumer key'],
                  consumer_secret=data['consumer secret'],
                  access_token_key=data['access token key'],
                  access_token_secret=data['access token secret'])
'''

def post_tweet():

    #content =

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


content = scrap_wikipedia.wiki_content()

process_tweet(content)
