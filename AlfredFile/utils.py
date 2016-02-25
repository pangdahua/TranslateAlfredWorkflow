#-*- coding:utf-8

import urllib
import json
import md5 as _md5

def get(url):
    fp = urllib.urlopen(url)
    content = fp.read()
    fp.close()

    return content

def json_decode(data):
    return json.loads(data)

def urlencode(word):
    return urllib.quote_plus(word)

def md5(str):
    return _md5.new(str).hexdigest()
