#-*- coding:utf-8
'''
   百度的翻译API
   申请 http://developer.baidu.com/console
'''

from utils import *
from time import time
import re

APP_ID = ''
SECRET_KEY = ''
SALT = int(time())

class BaiduTranslator():
    def translate(self, word):
        if re.match('[a-z]', word, re.I) is not None:
            _from,to = 'en', 'zh'
        else:
            _from,to = 'zh', 'en'

        apiUrl = 'http://api.fanyi.baidu.com/api/trans/vip/translate?from={0}&to={to}&q={word}&appid={appid}&salt={salt}&sign={sign}'.format(_from, to = to,word = word, appid = APP_ID,salt = SALT, sign = self._sign(SALT, word))
        resp = get(apiUrl)
        result = json_decode(resp)
        items = [(row['src'], row['dst'])for row in result['trans_result']]

        return items
    def _sign(self, salt, word):
        return md5('%s%s%s%s' % (APP_ID, word, salt, SECRET_KEY))

if __name__ == '__main__':
    import sys
    word = sys.argv[1].strip()
    trans = BaiduTranslator();
    print trans.translate(word)
