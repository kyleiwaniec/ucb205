import feedparser
from bs4 import BeautifulSoup
import json
import time
import sys


urls = {"top_news":"http://feeds.reuters.com/reuters/topNews", \
            "health": "http://feeds.reuters.com/reuters/healthNews", \
            "healthcare":"http://feeds.reuters.com/reuters/UShealthcareNews", \
            "science":"http://feeds.reuters.com/reuters/scienceNews", \
            "business":"http://feeds.reuters.com/reuters/businessNews", \
            "world": "http://feeds.reuters.com/Reuters/worldNews" }

etags = {"top_news": None, "health": None, "healthcare": None, "science": None, "business":None, "world":None}

done = False

while not done:
    for k, v in urls.items():
        if etags[k]:
            d = feedparser.parse(v, etag=etags[k])
        else:
            d = feedparser.parse(v)
            for e in d.entries:
                doc = json.dumps({"category":k, "title":e.title.strip(), "summary":BeautifulSoup(e.summary).text.strip()})
                print doc
        sys.stdout.flush()
        etags[k] = d.etag
        time.sleep(10)
