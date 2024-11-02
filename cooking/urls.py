from django.urls import path

from cooking.views import index

app_name = "cooking"

urlpatterns = [
    path("", index)
]