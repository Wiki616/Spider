# -*- coding: utf-8 -*-
# Author : Wiki_ki
# 简单的baidu贴吧爬虫框架

import urllib
import urllib2

url = 'http://tieba.baidu.com/p/3847106695'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'
values = {'name' : 'Wiki',
          'location' : 'fdu'}
headers = {'User-agent' : user_agent}
data = urllib.urlencode(values)
req = urllib2.Request(url,data,headers)
response = urllib2.urlopen(req)
content = response.read().decode('utf-8').encode('gbk')
print content
