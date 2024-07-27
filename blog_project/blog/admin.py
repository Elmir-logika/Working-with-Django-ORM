from django.contrib import admin

# _______________________.

from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)

