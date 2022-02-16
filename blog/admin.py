from django.contrib import admin

from .models import Post, Comment
# Post Model
admin.site.register(Post)
# Comment Model
admin.site.register(Comment)
