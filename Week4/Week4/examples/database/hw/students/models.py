from django.db import models

class Student(models.Model):
    number = models.IntegerField()
    name = models.TextField(max_length=20)
    email = models.TextField(max_length=50)


# Create your models here.
