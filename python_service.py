import urllib
import os
import time
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/trump-feed')
def rss():    
    RSS_URLS = 'https://twitrss.me/twitter_user_to_rss/?user=realDonaldTrump'
    res = urllib.urlopen(RSS_URLS)
    data = res.read()
    return str(data)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
