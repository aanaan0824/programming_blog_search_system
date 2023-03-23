from django.shortcuts import render
from students.models import Student

def index(request):
    Student.objects.all().delete()
    Student.objects.get_or_create(name="Zhang San", email="zhangsan@gmail.com", number=1)
    Student.objects.get_or_create(name="Li Si", email="lisi@thu.edu.cn", number=2)
    Student.objects.get_or_create(name="Wang Wu", email="wangwu@sina.cn", number=3)
    Student.objects.get_or_create(name="Wang Wu", email="wangwu@sina.cn", number=3)
    Student.objects.create(name="Wang Wu", email="wangwu@sina.cn", number=3)
    Student.objects.get_or_create(name="wang wu", email="wangwu@sina.cn", number=0)

    students = Student.objects.all()
    return render(request, 'list1.html', {'address': students})

def wangwu(request):
    print(Student.objects.filter(name='Li Si').update(name="wanG wU"))
    students = Student.objects.filter(name__iexact='wang wu')    #大小写不敏感
    students = students.order_by("number")
    return render(request, 'list1.html', {'address': students})