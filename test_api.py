#!/usr/bin/env python

import json
import twitter

filename = 'cred.json'
with open(filename) as f:
    data = json.load(f)

api = twitter.Api(consumer_key=data['consumer key'],
                  consumer_secret=data['consumer secret'],
                  access_token_key=data['access token key'],
                  access_token_secret=data['access token secret'])

print(api.VerifyCredentials())
