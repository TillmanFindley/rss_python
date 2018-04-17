import urllib
import os
import time
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/trump-feed')
def rss():  
    feeds = []
    RSS = 'http://thehill.com/rss/syndicator/19110'
    
    res = urllib.urlopen(RSS)
    data = res.read()
    return data
        
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
