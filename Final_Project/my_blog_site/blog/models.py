from django.db import models


class BlogInfo(models.Model):

    blogid = models.BigIntegerField()
    writerAge = models.CharField(max_length=20)
    writerBlogNum = models.IntegerField()
    writerCollect = models.IntegerField()
    writerComment = models.IntegerField()
    writerFan = models.IntegerField()
    writerGrade = models.CharField(max_length=20)
    writerIntegral = models.IntegerField()
    writerName = models.TextField()
    writerRankWeekly = models.IntegerField()
    writerRankTotal = models.IntegerField()
    writerProfileAdress = models.TextField()
    writerThumb = models.BigIntegerField()
    writerVisitNum = models.BigIntegerField()
    blog_read_count = models.BigIntegerField()
    blog_time = models.TextField()
    blog_title = models.TextField()
    content = models.TextField()

    cpp = models.SmallIntegerField(default=0)
    csharp = models.SmallIntegerField(default=0)
    java = models.SmallIntegerField(default=0)
    javascript = models.SmallIntegerField(default=0)
    php = models.SmallIntegerField(default=0)
    sqll = models.SmallIntegerField(default=0)
    python = models.SmallIntegerField(default=0)
    first_tag = models.CharField(max_length=20, default='Others')
    summa = models.TextField(default=None)
    time = models.DateTimeField(default='2000-01-01 00:00:00')

    def __str__(self):
        return self.blogid


class comment(models.Model):

    blog = models.ForeignKey(BlogInfo, on_delete=models.CASCADE)
    name = models.TextField()
    content = models.TextField()




