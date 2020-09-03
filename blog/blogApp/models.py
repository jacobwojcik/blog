from django.db import models

# Create your models here.


class Post(models.Model):
    post_author = models.CharField(max_length=50)
    post_body = models.CharField(max_length=5000)
    post_date = models.DateTimeField('date published')

    def ___str__(self):
        return self.post_body
