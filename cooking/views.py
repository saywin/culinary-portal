from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Post, Category


def index(request: HttpRequest) -> HttpResponse:
    """Для головної сторінки"""
    posts = Post.objects.all()

    context = {
        "title": "Головна сторінка",
        "posts": posts
    }
    return render(request, "cooking/index.html", context)