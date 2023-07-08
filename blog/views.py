from datetime import date
from django.shortcuts import render
from django.http import HttpResponse

all_posts = []

def get_date(post):
    return post['date']


def starting_page(request):
    """
    A view function to handle the starting page of the blog.
    """
    
    # Sort posts by date and get the latest 3
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
