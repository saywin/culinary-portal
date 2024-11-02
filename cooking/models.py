from django.db import models


class Category(models.Model):
    """Категорія новин"""

    title = models.CharField(max_length=255)


class Post(models.Model):
    """Для постів"""

    title = models.CharField(max_length=255)
    content = models.TextField(default="Скоро буде стаття...")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)
    watched = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
