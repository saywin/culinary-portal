from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Post, Category
from django.db.models import F


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


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """Сторінка статті"""
    article = Post.objects.get(pk=pk)
    recommendation = Post.objects.order_by("-watched")[:5]
    Post.objects.filter(pk=pk).update(watched=F("watched") + 1)
    context = {"title": article.title, "post": article, "recommend": recommendation}
    return render(request, "cooking/article_detail.html", context)
