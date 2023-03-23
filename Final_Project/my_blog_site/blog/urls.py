from django.urls import path, re_path
from . import views
#from my_blog_site.settings import MEDIA_ROOT
#from django.views.static import serve

app_name='blog'
urlpatterns = [
    path('hello/', views.index, name='index'),
    path('<int:blog_id>/', views.detail_index, name='detailindex'),
    path('', views.homepage_index, name='noneindex'),
    path('All/<int:page_id>/', views.all_list_index, name='alllistindex'),
    path('C++/<int:page_id>/', views.cpp_list_index, name='cpplistindex'),
    path('PHP/<int:page_id>/', views.php_list_index, name='phplistindex'),
    path('SQL/<int:page_id>/', views.sql_list_index, name='sqllistindex'),
    path('Csharp/<int:page_id>/', views.csharp_list_index, name='csharplistindex'),
    path('Java/<int:page_id>/', views.java_list_index, name='javalistindex'),
    path('JavaScript/<int:page_id>/', views.javascript_list_index, name='javascriptlistindex'),
    path('Python/<int:page_id>/', views.python_list_index, name='pythonlistindex'),
    path('Others/<int:page_id>/', views.others_list_index, name='otherslistindex'),
    path('Result/',views.result_index,name='resultlistindex')
]
