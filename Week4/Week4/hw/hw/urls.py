"""hw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import hw, time, add, list, lists, reply
from . import settings
from . import studenturl
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', hw.index),
    path(r'hw/', hw.indexhw),
    path(r'time/', time.current_datetime),
    re_path(r'^time/plus/(\d{1,2})/$', time.hours_ahead),
    path(r'add/', add.index),
    path(r'list/', list.index),
    path(r'list2/', lists.index),
    path(r'hw/formsubmit/', reply.index),
    path(r'students/', studenturl.index),
    path(r'wangwu/', studenturl.wangwu),    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
