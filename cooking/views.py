from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Post, Category


def index(request: HttpRequest) -> HttpResponse:
    """Для головної сторінки"""
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        "title": "Головна сторінка",
        "posts": posts,
        "categories": categories,
    }
    return render(request, "cooking/index.html", context)


def category_list(request: HttpRequest, pk: int) -> HttpResponse:
    """Реакція на натискання кнопки категорії"""
    posts = Post.objects.filter(category_id=pk)
    categories = Category.objects.all()
    context = {
        "title": posts[0].category,
        "posts": posts,
        "categories": categories,
    }
    return render(request, "cooking/index.html", context)
