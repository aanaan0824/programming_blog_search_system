import urllib.request
req = urllib.request.Request('http://www.python.org/')
response = urllib.request.urlopen(req) 
the_page = response.read() 
the_page = the_page.decode('utf-8')
with open('pythonHome2.html', 'w', encoding='utf-8') as f:
    f.write(the_page)
    f.close()
print(the_page)
