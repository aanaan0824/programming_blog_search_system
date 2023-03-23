1 在命令行下，在HW目录，键入python manage.py startapp testDB
2 修改settings.py:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'testDB',
]
3 修改testDB/models.py
4 修改testDB/admin.py
5 键入python manage.py makemigrations
6 键入python manage.py migrate
7 修改urls.py，并定义数据库操作的视图函数