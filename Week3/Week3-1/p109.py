#coding=utf-8

import urllib
import urllib.request
url = 'http://dict.youdao.com/search'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
values = {'q' : 'python'}
data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data.encode('ascii'), headers)
response = urllib.request.urlopen(req)
the_page = response.read()
the_page = the_page.decode('utf-8')
with open('python.html', 'w', encoding='utf-8') as f:
    f.write(the_page)
    f.close()
print(the_page)
