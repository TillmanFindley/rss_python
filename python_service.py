import feedparser
import pprint
import re
import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

feeds = []
RSS_URLS = ['https://twitrss.me/twitter_user_to_rss/user=realDonaldTrump','http://thehill.com/rss/syndicator/19110',
            'http://thehill.com/taxonomy/term/1132/feed',
            'http://thehill.com/taxonomy/term/1130/feed','http://thehill.com/taxonomy/term/1131/feed',
            'http://thehill.com/taxonomy/term/1630/feed',
            'http://thehill.com/taxonomy/term/1778/feed','http://thehill.com/rss/syndicator/19109']
@app.route('/')
def rss():    
    for url in RSS_URLS:
        feeds.append(feedparser.parse(url))

    for feed in feeds:
        for post in feed['entries']:
            print post
            return post
        
        
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))