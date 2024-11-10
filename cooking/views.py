from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Category
from django.db.models import F
from .forms import PostAddForm, LoginForm, RegistrationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views import generic


# def index(request: HttpRequest) -> HttpResponse:
#     """Для головної сторінки"""
#     posts = Post.objects.all()
#     categories = Category.objects.all()
#     context = {
#         "title": "Головна сторінка",
#         "posts": posts,
#         "categories": categories,
#     }
#     return render(request, "cooking/_index.html", context)


class Index(generic.ListView):
    """Для головної сторінки"""

    model = Post
    context_object_name = "posts"
    template_name = "cooking/_index.html"
    extra_context = {"title": "Головна сторінка"}


# def category_list(request: HttpRequest, pk: int) -> HttpResponse:
#     """Реакція на натискання кнопки категорії"""
#     posts = Post.objects.filter(category_id=pk)
#     categories = Category.objects.all()
#     context = {
#         "title": posts[0].category,
#         "posts": posts,
#         "categories": categories,
#     }
#     return render(request, "cooking/_index.html", context)


class ArticleByCategory(Index):
    """Реакція на натискання кнопки категорії"""

    def get_queryset(self):
        return Post.objects.filter(
            category_id=self.kwargs["pk"], is_published=True
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()  # context = {}
        category = Category.objects.get(pk=self.kwargs["pk"])
        context["title"] = category.title
        return context


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     """Сторінка статті"""
#     article = Post.objects.get(pk=pk)
#     recommendation = Post.objects.exclude(pk=pk).order_by("-watched")[:5]
#     Post.objects.filter(pk=pk).update(watched=F("watched") + 1)
#     context = {
#         "title": article.title,
#         "post": article,
#         "recommend": recommendation,
#     }
#     return render(request, "cooking/_article_detail.html", context)

class PostDetail(generic.DetailView):
    """Сторінка статті"""
    model = Post
    template_name = "cooking/_article_detail.html"

    def get_queryset(self):
        post = Post.objects.filter(pk=self.kwargs["pk"])
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data()  # context = {}
        Post.objects.filter(pk=self.kwargs["pk"]).update(watched=F("watched") + 1)
        post = Post.objects.get(pk=self.kwargs["pk"])
        recommend = Post.objects.exclude(pk=self.kwargs["pk"]).order_by("-watched")[:5]
        context["title"] = post.title
        context["recommend"] = recommend
        return context


# def add_post(request: HttpRequest) -> HttpResponse:
#     """Додавання статті від користувача"""
#     if request.method == "POST":
#         form = PostAddForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = Post.objects.create(**form.cleaned_data)
#             post.save()
#             return redirect("cooking:post_detail", post.pk)
#     else:
#         form = PostAddForm()
#     context = {"title": "Додати статтю", "form": form}
#     return render(request, "cooking/_acticle_add_form.html", context)

class AddPost(generic.CreateView):
    """Додавання статті від користувача"""
    form_class = PostAddForm
    template_name = "cooking/_article_add_form.html"
    extra_context = {"title": "Додати статтю"}


class UpdatePost(generic.UpdateView):
    """Редагування статті"""
    model = Post
    form_class = PostAddForm
    template_name = "cooking/_article_add_form.html"


def user_login(request: HttpRequest) -> HttpResponse:
    """Аутентифікація користувача"""
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(
                request, "Ви успішно приєдналися до свого облікового запису"
            )
            return redirect("cooking:index")
    else:
        form = LoginForm()

    context = {"title": "Авторизація користувача", "form": form}
    return render(request, "cooking/_login_form.html", context)


def user_logout(request: HttpRequest) -> HttpResponse:
    """Вихід користувача"""
    logout(request)
    messages.success(request, "Ви успішно вийшли з облікового запису")
    return redirect("cooking:index")


def user_register(request: HttpRequest) -> HttpResponse:
    """Реєстрація користувача"""
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ви успішно зареєстрували акаунт")
            return redirect("cooking:login")
    else:
        form = RegistrationForm()

    context = {"title": "Реєстрація користувача", "form": form}
    return render(request, "cooking/_register_form.html", context)
