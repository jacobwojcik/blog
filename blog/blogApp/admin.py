from django.contrib import admin
from .models import Post

admin.site.site_header = "Blog Admin"

# customize admin area
# Register your models here.

admin.site.register(Post)
