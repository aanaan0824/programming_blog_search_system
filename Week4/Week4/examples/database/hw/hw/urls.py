"""hw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import hw, time, add, list, lists, reply, studenturl
import django
#import setting
from . import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hw.index),
    path('hw/', hw.indexhw),
    path('time/', time.current_datetime),
    re_path('time/plus/(\d{1,2})/', time.hours_ahead),
    path(r'add/', add.index),
    path('list/', list.index),
    path(r'list1/', list.index),
    path(r'list2/', lists.index),
    path(r'students/', studenturl.index),
    path(r'wangwu/', studenturl.wangwu),
    # url(r'^csv/(\w+)/$', csv.output),
    path(r'hw/formsubmit/', reply.index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 