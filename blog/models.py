from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Tag(models.Model):
    """
    Tag model for blog posts.
    """
    caption = models.CharField(max_length=20)

    def __str__(self):
        """Return string representation of tag."""
        return self.caption


class Author(models.Model):
    """This model represents an author and it's properties."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        """Return full name of author."""
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """Return string representation of author."""
        return self.full_name()


class Post(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tags = models.ManyToManyField(Tag)
