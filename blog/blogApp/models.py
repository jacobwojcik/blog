from django.db import models
import os
# Create your models here.


# def get_image_path(instance, filename):
#     upload_to = 'blogApp/static/posts/images/posts'
#     return os.path.join(upload_to, filename)


class Post(models.Model):
    post_author = models.CharField(max_length=50)
    post_title = models.CharField(max_length=50)
    post_image = models.ImageField(upload_to='post_images', null=True)
    post_body = models.CharField(max_length=5000)
    post_date = models.DateTimeField('date published')

    def ___str__(self):
        return self.post_body
