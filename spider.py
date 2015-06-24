# -*- coding: utf-8 -*-
# Author : Wiki_ki
# 简单的baidu贴吧爬虫框架

import urllib
import urllib2
import re
from config import url , user_agent , values , url_root

def getLinks(content):
    p = re.compile(r'\/p\/\d+')
    r = p.findall(content)
    return r

def getContent(url):
    req = urllib2.Request(url,data,headers)
    response = urllib2.urlopen(req)
    content = response.read().decode('utf-8').encode('gbk')
    print 'ok'

headers = {'User-agent' : user_agent}
data = urllib.urlencode(values)
req = urllib2.Request(url,data,headers)
response = urllib2.urlopen(req)
content = response.read()
s = getLinks(content)
dict = {}
for suffix in s:
    if (not dict.has_key(suffix)):
        getContent(url_root + suffix)
        dict[suffix] = True
print dict
#print content
