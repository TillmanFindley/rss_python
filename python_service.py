import urllib
import os
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/trump-feed')
def rss():  
    twitter = 'https://twitrss.me/twitter_user_to_rss/?user=realDonaldTrump'
    res1 = urllib.urlopen(twitter)
    data1 = res1.read()
    return data1

    RSS = 'http://abcnews.go.com/abcnews/mostreadstories'
    res2 = urllib.urlopen(RSS)
    data2 = res2.read()
    return data2
    
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
