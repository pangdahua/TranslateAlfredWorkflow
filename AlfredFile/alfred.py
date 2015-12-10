#-*- coding:utf-8
'''
    对外请求的接口
'''

import sys
from baidutrans import *
from translate import *
from feedback import *

result = Feedback()
word = sys.argv[1]

translator = TranslateDelegate(BaiduTranslator()) 
tranResults = translator.translate(word)

if len(tranResults) > 0:
    for row in tranResults:
        item = row[0] + " " + row[1]
        result.add_item(item, subtitle = "")
else:
    result.add_item("Can't find relate information")

print result
