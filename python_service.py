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
        
if __name__ == "__main__":
    app.run(debug=True)
