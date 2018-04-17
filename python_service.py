import feedparser
import pprint
import re
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def rss(): 
    feeds = []
    RSS_URLS = ['https://twitrss.me/twitter_user_to_rss/user=realDonaldTrump','http://thehill.com/rss/syndicator/19110',
            'http://thehill.com/taxonomy/term/1132/feed','http://thehill.com/taxonomy/term/1130/feed',
            'http://thehill.com/taxonomy/term/1131/feed','http://thehill.com/taxonomy/term/1630/feed',
            'http://thehill.com/taxonomy/term/1778/feed','http://thehill.com/rss/syndicator/19109']
    for url in RSS_URLS:
        feeds.append(feedparser.parse(url))
    for feed in feeds:
        for post in feed['entries']:
            print post
   
        
        
if __name__ == '__main__':
    app.run(debug=True)