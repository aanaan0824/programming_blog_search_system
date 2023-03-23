import urllib.request
response = urllib.request.urlopen('http://python.org/')
html = response.read()
the_page = html.decode('utf-8')
with open('pythonHome.html', 'w', encoding='utf-8') as f:
    f.write(the_page)
    f.close()
print(the_page)
print(html)
