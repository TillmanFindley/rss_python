import urllib
import os
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/trump-feed')
def rss():  
    twitter = 'https://twitrss.me/twitter_user_to_rss/?user=realDonaldTrump'
    
    res1 = urllib.urlopen(twitter)
    data1 = res1.read()
    print data1
    
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
