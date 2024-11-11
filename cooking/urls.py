from django.urls import path
from django.views.decorators.cache import cache_page
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

from cooking import views

app_name = "cooking"

urlpatterns = [
    path("", cache_page(60 * 15)(views.Index.as_view()), name="index"),
    path(
        "category/<int:pk>/",
        views.ArticleByCategory.as_view(),
        name="category_list"
    ),
    path("post/<int:pk>", views.PostDetail.as_view(), name="post_detail"),
    path("add_arcticle/", views.AddPost.as_view(), name="add_post"),
    path("post/<int:pk>/update/", views.UpdatePost.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", views.DeletePost.as_view(), name="post_delete"),
    path("search/", views.SearchResult.as_view(), name="search"),
    path(
        "password/",
        views.UserChangePassword.as_view(),
        name="change_password",
    ),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.user_register, name="register"),
    path("add_comment/<int:post_id>/", views.add_comment, name="add_comment"),
    path("profile/<int:user_id>/", views.profile, name="profile"),

    # API
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("posts/api/", views.CookingAPI.as_view(), name="cooking_api"),
    path("posts/api/<int:pk>", views.CookingAPIDetail.as_view(), name="cooking_api_detail"),
    path("categories/api/", views.CategoryAPI.as_view(), name="category_api"),
    path("categories/api/<int:pk>", views.CategoryAPIDetail.as_view(), name="category_api_detail"),
]
