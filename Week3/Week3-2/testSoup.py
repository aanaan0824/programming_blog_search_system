import bs4
from bs4 import BeautifulSoup

markup = """
<HTML> <HEAD>
 <meta http-equiv="Content-Type"  content="text/html; charset=gb2312">
<TITLE>清华大学计算机系</TITLE> </HEAD>
<BODY   bgcolor= yellow>
<P>这是一个测试段落</P>
<div class='div-class element-class' id='thediv'>
<a href="http://www.example.com/alpha" id='a1'> Alpha </a>
<a href="http://www.example.com/beta" id='a2'> Beta </a>
<a href="http://www.example.com/gamma" id='a3'> Gamma </a>
</div>
</BODY></HTML> 
"""
soup = BeautifulSoup(markup)	# 默认使用内置解析器
print(soup.prettify())	#打印美化后（标准格式）的HTML
print(soup.title.name)
print(soup.title.string)
print(soup.p)
print(soup.a)
print(soup.div['class'])
print(soup.p.parent.name)
print(soup.get_text())
print("soup.find_all(\'a\'):", soup.find_all('a'))
print("soup.find(id=\'a1\'):", soup.find(id='a1'))
print("soup.find_all(text=\'Alpha\'):", soup.find_all(text=' Alpha '))
print("soup.find(text=\'Alpha\').parent:", soup.find(text=' Alpha ').parent)

sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>")
print(sibling_soup.b.next_sibling)
print(sibling_soup.c.previous_sibling)


