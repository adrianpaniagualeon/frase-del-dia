#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import tweepy
import json
import os

CONSUMER_KEY= os.environ['CONSUMER_KEY']
CONSUMER_SECRET =os.environ['CONSUMER_SECRET']
ACCESS_TOKEN= os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET =os.environ['ACCESS_TOKEN_SECRET']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

r = requests.get("https://frasedeldia.azurewebsites.net/api/phrase")
open('frase.json', 'w').write(r.text)
f = open('frase.json')
json_file = json.load(f)
json_str = json.dumps(json_file)
resp2 = json.loads(json_str)
frase = resp2 ["phrase"]
autor = resp2 ["author"]
tweet = '"'+frase+'"-'+autor
api.update_status(tweet)