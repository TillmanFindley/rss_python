import urllib
import os
import time
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/trump-feed')
def rss():    
    RSS_URLS = ['https://twitrss.me/twitter_user_to_rss/?user=realDonaldTrump','http://thehill.com/rss/syndicator/19110',
                'http://thehill.com/taxonomy/term/1132/feed','http://thehill.com/taxonomy/term/1130/feed',
                'http://thehill.com/taxonomy/term/1131/feed','http://thehill.com/taxonomy/term/1630/feed',
                'http://thehill.com/taxonomy/term/1778/feed','http://thehill.com/rss/syndicator/19109']
    for url in RSS_URLS:
        res = urllib.urlopen(url)
        data = res.read()
        print data
        
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
