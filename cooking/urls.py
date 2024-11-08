from django.urls import path

from cooking.views import index, category_list, post_detail

app_name = "cooking"

urlpatterns = [
    path("", index, name="index"),
    path("category/<int:pk>/", category_list, name="category_list"),
    path("post/<int:pk>", post_detail, name="post_detail"),
]
