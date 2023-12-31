from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag


def starting_page(request):
    """
    A view function to handle the starting page of the blog.
    """
    # Sort posts by date and get the latest 3
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    """
    View function to handle all posts.
    """
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    """
    Return a single post based on the post's slug
    """

    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })
