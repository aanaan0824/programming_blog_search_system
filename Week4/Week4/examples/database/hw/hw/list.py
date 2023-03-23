from django.shortcuts import render

address=[
    {'name':'San Zhang', 'email':'zhangsan@gmail.com'},
    {'name':'Si Li', 'email':'lisi@thu.edu.cn'},
    {'name':'Wu Wang', 'email':'wangwu@sina.cn'}
    ]    

def index(request):
    return render(request, 'list1.html', {'address': address})