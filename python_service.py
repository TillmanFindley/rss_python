import urllib
import os
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/trump-feed')
def rss():  
    twitter = 'https://twitrss.me/twitter_user_to_rss/?user=realDonaldTrump'
    RSS = 'http://thehill.com/rss/syndicator/19110'
    
    res1 = urllib.urlopen(twitter)
    data1 = res1.read()
    print data1
    
if __name__ == "__main__":
    app.run(debug=True)
