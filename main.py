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

r = requests.get("https://proverbia.net/frase-del-dia")
block = r.text.split('<blockquote class="bsquote">')[1].split("</em>")[0]
frase = block.split("<p>")[1].split("</p>")[0]
frase = frase.replace("<br>","")
frase = frase.replace("<br />","")
autor = block.split('<a title="Frases de ')[1].split('"')[0]

tweet = '"'+frase+'"- '+autor
api.update_status(tweet)