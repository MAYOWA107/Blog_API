from django.db import models



class Article(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100, null=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.title