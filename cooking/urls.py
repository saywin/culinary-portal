from django.urls import path

from cooking.views import (
    user_login,
    user_logout,
    user_register,
    Index, ArticleByCategory,
    PostDetail,
    AddPost,
)

app_name = "cooking"

urlpatterns = [
    # path("", index, name="index"),
    path("", Index.as_view(), name="index"),
    # path("category/<int:pk>/", category_list, name="category_list"),
    path("category/<int:pk>/", ArticleByCategory.as_view(), name="category_list"),
    # path("post/<int:pk>", post_detail, name="post_detail"),
    path("post/<int:pk>", PostDetail.as_view(), name="post_detail"),
    # path("add_arcticle/", add_post, name="add_post"),
    path("add_arcticle/", AddPost.as_view(), name="add_post"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", user_register, name="register"),
]
