from django.contrib import admin

# Register your models here.
from testDB import models
admin.site.register(models.Student)