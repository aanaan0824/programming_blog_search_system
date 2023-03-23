from django.template import loader, Context
from django.http import HttpResponse

address=[
    {'name':'Zhang San', 'email':'zhangsan@gmail.com'},
    {'name':'Li Si', 'email':'lisi@thu.edu.cn'},
    {'name':'Wang Wu', 'email':'wangwu@sina.cn'}
    ]    
def index(request):
    response = HttpResponse(content_type='text/html') 
    t = loader.get_template('list2.html') 
    # c = Context({ 'address': address})
    # response.write(t.render(c))
    response.write(t.render({'address': address}))
    return response
