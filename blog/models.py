from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()


class Post(models.Model):
    """
    Model representing a blog post.
    """
    title: models.CharField(max_length=150)
    excerpt: models.CharField(max_length=200)
    image_name: models.CharField(max_length=200, null=True)
    slug = models.SlugField(unique=True, db_index=True)
    content: models.TextField(MinLengthValidator(10))
    date: models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tags = models.ManyToManyField(Tag)
