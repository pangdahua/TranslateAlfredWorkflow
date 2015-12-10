#-*- coding:utf-8
'''
   百度的翻译API
   申请 http://developer.baidu.com/console
'''

from utils import *

API_KEY = 'AsIikT9sOqHyHzU6aiuBoOVg'

class BaiduTranslator():
    def translate(self, word):
        apiUrl = 'http://openapi.baidu.com/public/2.0/bmt/translate?client_id=%s&q=%s&from=auto&to=auto' % (API_KEY, urlencode(word))
        resp = get(apiUrl)
        result = json_decode(resp)
        items = [(row['src'], row['dst'])for row in result['trans_result']]

        return items
    

if __name__ == '__main__':
    import sys
    word = sys.argv[1].strip()
    trans = BaiduTranslator();
    print trans.translate(word)
