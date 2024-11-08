from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Category
from django.db.models import F
from .forms import PostAddForm, LoginForm
from django.contrib.auth import login, logout


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


def add_post(request: HttpRequest) -> HttpResponse:
    """Додавання статті від користувача"""
    if request.method == "POST":
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            post.save()
            return redirect("cooking:post_detail", post.pk)
    else:
        form = PostAddForm()
    context = {"title": "Додати статтю", "form": form}
    return render(request, "cooking/acticle_add_form.html", context)


def user_login(request: HttpRequest) -> HttpResponse:
    """Аутентифікація користувача"""
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("cooking:index")
    else:
        form = LoginForm()

    context = {
        "title": "Авторизація користувача",
        "form": form
    }
    return render(request, "cooking/login_form.html", context)


def user_logout(request: HttpRequest) -> HttpResponse:
    """Вихід користувача"""
    logout(request)
    return redirect("cooking:index")
