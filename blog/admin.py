from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post)
