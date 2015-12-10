#-*- coding:utf-8

import urllib
import json

def get(url):
    fp = urllib.urlopen(url)
    content = fp.read()
    fp.close()

    return content

def json_decode(data):
    return json.loads(data)

def urlencode(word):
    return urllib.quote_plus(word)
