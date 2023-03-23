from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from.models import BlogInfo, comment
import random
from django.core.paginator import Paginator
from collections import Counter
import time

global key, stype, lan_opt, blognum, time_start, time_end

def get_tags(one: BlogInfo):
    tags=[]
    if (one.cpp==1):
        tags.append('C++')
    if (one.csharp == 1):
        tags.append('C#')
    if (one.java == 1):
        tags.append('Java')
    if (one.javascript == 1):
        tags.append('JavaScript')
    if (one.python == 1):
        tags.append('Python')
    if (one.php == 1):
        tags.append('PHP')
    if (one.sqll == 1):
        tags.append('SQL')
    i=0
    for tmp in tags:
        i+=1
    if (i==0):
        tags.append('Others')
    return tags

def index(request):
    return HttpResponse("Hello, world! You're at the polls index.")

def homepage_index(request):
    if request.method== "GET" :
        last=BlogInfo.objects.count()-1

        index1 = random.randint(0, last)
        index2 = random.randint(0, last-1)
        if index2 == index1:
            index2 = random.randint(0, last-1)

        randint_list = []
        for i in range(0, 18):
            randint_list.append(random.randint(0, last))
        bloglist = []
        for i in randint_list:
            bloglist.append(BlogInfo.objects.all()[i])
        blog1 = BlogInfo.objects.all()[index1]
        blog2 = BlogInfo.objects.all()[index2]
        context = {"bloglist": bloglist,
                   "blog1": blog1,
                   "blog2": blog2}
        return render(request, "homepage.html",context)
    if request.method == "POST" :
        global key
        key=request.POST.get("email")
        global stype
        stype = 1
        if(request.POST.get("dueto") != None):
            stype=request.POST.get("dueto")
        global lan_opt
        lan_opt=request.POST.get("lan")
        global time_start
        time_start=time.time()
        return redirect(reverse("blog:resultlistindex"))

def detail_index(request, blog_id):
    if (request.method == 'GET'):
        blog_data = BlogInfo.objects.filter(blogid=blog_id)[0]
        tags = get_tags(blog_data)
        commentset=blog_data.comment_set.all()
        context = {'blog_data': blog_data,
                   'tags': tags,
                   'commentset':commentset}
        return render(request, "detail.html", context)
    else:
        content1=request.POST.get("comment")
        audi=request.POST.get("audience")
        a=comment(content=content1,name=audi,blog=BlogInfo.objects.filter(blogid=blog_id)[0])
        a.save()
        blog_data = BlogInfo.objects.filter(blogid=blog_id)[0]
        tags = get_tags(blog_data)
        commentset = blog_data.comment_set.all()
        context = {'blog_data': blog_data,
                   'tags': tags,
                   'commentset': commentset}
        return render(request, "detail.html", context)

def all_list_index(request, page_id):
    if(request.method=='GET'):
        bloglist = BlogInfo.objects.all()[100*(page_id-1):100*page_id]
        #last_page = BlogInfo.objects.count()/100+1
        context = {"bloglist": bloglist,
                   "page_id": page_id,
                   "last_page": 51}
        return render(request, "list_page.html", context)
    else:
        pagenum=request.POST.get("pagenum")
        if not pagenum:
            return HttpResponse("页数输入错误，请返回重新输入！")
        pagenum=int(pagenum)
        if pagenum<=0 or pagenum>51:
            return HttpResponse("页数输入错误，请返回重新输入！")
        else:
            return redirect(reverse("blog:alllistindex",args=[pagenum]))

def cpp_list_index(request, page_id):
    if (request.method == 'GET'):
        bloglist = BlogInfo.objects.filter(cpp=1)[100 * (page_id - 1):100 * page_id]
        # last_page = BlogInfo.objects.count()/100+1
        context = {"bloglist": bloglist,
                   "page_id": page_id,
                   "last_page": 10}
        return render(request, "list_page.html", context)
    else:
        pagenum=request.POST.get("pagenum")
        if not pagenum:
            return HttpResponse("页数输入错误，请返回重新输入！")
        pagenum=int(pagenum)
        if pagenum<=0 or pagenum>10:
            return HttpResponse("页数输入错误，请返回重新输入！")
        else:
            return redirect(reverse("blog:cpplistindex",args=[pagenum]))

def csharp_list_index(request, page_id):
    if (request.method == 'GET'):
        bloglist = BlogInfo.objects.filter(csharp=1)[100 * (page_id - 1):100 * page_id]
        # last_page = BlogInfo.objects.count()/100+1
        context = {"bloglist": bloglist,
                   "page_id": page_id,
                   "last_page": 7}
        return render(request, "list_page.html", context)
    else:
        pagenum=request.POST.get("pagenum")
        if not pagenum:
            return HttpResponse("页数输入错误，请返回重新输入！")
        pagenum=int(pagenum)
        if pagenum<=0 or pagenum>7:
            return HttpResponse("页数输入错误，请返回重新输入！")
        else:
            return redirect(reverse("blog:csharplistindex",args=[pagenum]))

def java_list_index(request, page_id):
    if (request.method == 'GET'):
        bloglist = BlogInfo.objects.filter(java=1)[100 * (page_id - 1):100 * page_id]
        # last_page = BlogInfo.objects.count()/100+1
        context = {"bloglist": bloglist,
                   "page_id": page_id,
                   "last_page": 11}
        return render(request, "list_page.html", context)
    else:
        pagenum = request.POST.get("pagenum")
        if not pagenum:
            return HttpResponse("页数输入错误，请返回重新输入！")
        pagenum = int(pagenum)
        if pagenum <= 0 or pagenum > 11:
            return HttpResponse("页数输入错误，请返回重新输入！")
        else:
            return redirect(reverse("blog:javalistindex", args=[pagenum]))

def python_list_index(request, page_id):
    if (request.method == 'GET'):
        bloglist = BlogInfo.objects.filter(python=1)[100 * (page_id - 1):100 * page_id]
        # last_page = BlogInfo.objects.count()/100+1
        context = {"bloglist": bloglist,
                   "page_id": page_id,
                   "last_page": 9}
        return render(request, "list_page.html", context)
    else:
        pagenum = request.POST.get("pagenum")
        if not pagenum:
            return HttpResponse("页数输入错误，请返回重新输入！")
        pagenum = int(pagenum)
        if pagenum <= 0 or pagenum > 9:
            return HttpResponse("页数输入错误，请返回重新输入！")
        else:
            return redirect(reverse("blog:pythonlistindex", args=[pagenum]))

def javascript_list_index(request, page_id):
    if (request.method == 'GET'):
        bloglist = BlogInfo.objects.filter(javascript=1)[100 * (page_id - 1):100 * page_id]
        # last_page = BlogInfo.objects.count()/100+1
        context = {"bloglist": bloglist,
                   "page_id": page_id,
                   "last_page": 6}
        return render(request, "list_page.html", context)
    else:
        pagenum = request.POST.get("pagenum")
        if not pagenum:
            return HttpResponse("页数输入错误，请返回重新输入！")
        pagenum = int(pagenum)
        if pagenum <= 0 or pagenum > 6:
            return HttpResponse("页数输入错误，请返回重新输入！")
        else:
            return redirect(reverse("blog:javascriptlistindex", args=[pagenum]))

def php_list_index(request, page_id):
    if (request.method == 'GET'):
        bloglist = BlogInfo.objects.filter(php=1)[100 * (page_id - 1):100 * page_id]
        # last_page = BlogInfo.objects.count()/100+1
        context = {"bloglist": bloglist,
                   "page_id": page_id,
                   "last_page": 7}
        return render(request, "list_page.html", context)
    else:
        pagenum = request.POST.get("pagenum")
        if not pagenum:
            return HttpResponse("页数输入错误，请返回重新输入！")
        pagenum = int(pagenum)
        if pagenum <= 0 or pagenum > 7:
            return HttpResponse("页数输入错误，请返回重新输入！")
        else:
            return redirect(reverse("blog:phplistindex", args=[pagenum]))

def sql_list_index(request, page_id):
    if (request.method == 'GET'):
        bloglist = BlogInfo.objects.filter(sqll=1)[100 * (page_id - 1):100 * page_id]
        # last_page = BlogInfo.objects.count()/100+1
        context = {"bloglist": bloglist,
                   "page_id": page_id,
                   "last_page": 11}
        return render(request, "list_page.html", context)
    else:
        pagenum = request.POST.get("pagenum")
        if not pagenum:
            return HttpResponse("页数输入错误，请返回重新输入！")
        pagenum = int(pagenum)
        if pagenum <= 0 or pagenum > 11:
            return HttpResponse("页数输入错误，请返回重新输入！")
        else:
            return redirect(reverse("blog:sqllistindex", args=[pagenum]))

def others_list_index(request, page_id):
    if (request.method == 'GET'):
        bloglist = BlogInfo.objects.filter(first_tag="Others")[100 * (page_id - 1):100 * page_id]
        # last_page = BlogInfo.objects.count()/100+1
        context = {"bloglist": bloglist,
                   "page_id": page_id,
                   "last_page": 11}
        return render(request, "list_page.html", context)
    else:
        pagenum = request.POST.get("pagenum")
        if not pagenum:
            return HttpResponse("页数输入错误，请返回重新输入！")
        pagenum = int(pagenum)
        if pagenum <= 0 or pagenum > 11:
            return HttpResponse("页数输入错误，请返回重新输入！")
        else:
            return redirect(reverse("blog:otherslistindex", args=[pagenum]))

def result_index(request):
    if (request.method == 'GET'):
        bloglist = BlogInfo.objects.filter(pk=0)
        if (lan_opt == None):
            bloglist = BlogInfo.objects.all()
        else:
            if ("cppcheck" in lan_opt) == True:
                bloglist = bloglist | BlogInfo.objects.filter(cpp=1)
            if ("csharpcheck" in lan_opt) == True:
                bloglist = bloglist | BlogInfo.objects.filter(csharp=1)
            if ("phpcheck" in lan_opt) == True:
                bloglist = bloglist | BlogInfo.objects.filter(php=1)
            if ("sqlcheck" in lan_opt) == True:
                bloglist = bloglist | BlogInfo.objects.filter(sqll=1)
            if ("pythoncheck" in lan_opt) == True:
                bloglist = bloglist | BlogInfo.objects.filter(python=1)
            if ("javacheck" in lan_opt) == True:
                bloglist = bloglist | BlogInfo.objects.filter(java=1)
            if ("javascriptcheck" in lan_opt) == True:
                bloglist = bloglist | BlogInfo.objects.filter(javascript=1)
            if ("otherscheck" in lan_opt) == True:
                bloglist = bloglist | BlogInfo.objects.filter(first_tag="Others")

        if key != None:
            bloglist = bloglist.filter(blog_title__icontains=key) | bloglist.filter(content__icontains=key)

        if stype == '1':
            bloglist=bloglist.order_by("time")
        elif stype == '2':
            bloglist=bloglist.order_by("-blog_read_count")
        else:
            bloglist = bloglist.order_by("-time")

        if bloglist != None :
            pag = Paginator(bloglist,50)
            pagenum = request.GET.get('pagenum')
            if pagenum==None :
                pagenum=1
            pagenum = int(pagenum)
            page=pag.get_page(pagenum)
            #print(type(bloglist))
            global blognum
            blognum=len(bloglist)
            bloglist=bloglist[50*(pagenum-1): 50*pagenum]
            global time_end
            global time_start
            time_end=time.time()
            context={
                'u':page,
                'bloglist':bloglist,
                'blognum':blognum,
                'time':time_end-time_start
            }
            return render(request,'result.html', context)
        else :
            HttpResponse("抱歉，我们没有搜索到符合条件的文章！")
    else:
        pagenum=request.POST.get("pagenum")
        if not pagenum:
            return HttpResponse("页码错误，请返回重新输入")
        pagenum = int(pagenum)
        if pagenum <= 0 or pagenum > blognum/50+1:
            return HttpResponse("页数输入错误，请返回重新输入！")
        else:
            return redirect(reverse("blog:resultlistindex")+"?pagenum="+str(pagenum))