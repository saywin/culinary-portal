from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from cooking.views import (
    user_login,
    user_logout,
    user_register,
    Index,
    ArticleByCategory,
    PostDetail,
    AddPost,
    UpdatePost,
    DeletePost,
    SearchResult,
    add_comment,
    profile,
    UserChangePassword,
    CookingAPI,
    CookingAPIDetail,
    CategoryAPIDetail,
    CategoryAPI,
)

app_name = "cooking"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path(
        "category/<int:pk>/",
        ArticleByCategory.as_view(),
        name="category_list"
    ),
    path("post/<int:pk>", PostDetail.as_view(), name="post_detail"),
    path("add_arcticle/", AddPost.as_view(), name="add_post"),
    path("post/<int:pk>/update/", UpdatePost.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", DeletePost.as_view(), name="post_delete"),
    path("search/", SearchResult.as_view(), name="search"),
    path(
        "password/",
        UserChangePassword.as_view(),
        name="change_password",
    ),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", user_register, name="register"),
    path("add_comment/<int:post_id>/", add_comment, name="add_comment"),
    path("profile/<int:user_id>/", profile, name="profile"),

    # API Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("posts/api/", CookingAPI.as_view(), name="cooking_api"),
    path("posts/api/<int:pk>", CookingAPIDetail.as_view(), name="cooking_api_detail"),
    path("categories/api/", CategoryAPI.as_view(), name="category_api"),
    path("categories/api/<int:pk>", CategoryAPIDetail.as_view(), name="category_api_detail"),
]
