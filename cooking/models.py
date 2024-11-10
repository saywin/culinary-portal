from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    """Категорія новин"""

    title = models.CharField(max_length=255, verbose_name="Назва категорії")

    class Meta:
        db_table = "category"
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def get_absolute_url(self):
        return reverse("cooking:category_list", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Post(models.Model):
    """Для постів"""

    title = models.CharField(max_length=255, verbose_name="Назва")
    content = models.TextField(
        default="Скоро буде стаття...", verbose_name="Контент"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата створення"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата оновлення"
    )
    photo = models.ImageField(
        upload_to="photos/", blank=True, null=True, verbose_name="Зображення"
    )
    watched = models.IntegerField(
        default=0, verbose_name="Кількість переглядів"
    )
    is_published = models.BooleanField(
        default=True, verbose_name="Опубліковано?"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Категорія",
    )

    class Meta:
        db_table = "post"
        verbose_name = "Пост"
        verbose_name_plural = "Пости"

    def get_absolute_url(self):
        return reverse("cooking:post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Коментарі к статтям"""
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Стаття"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Користувач"
    )
    text = models.TextField(verbose_name="Коментар")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")

    class Meta:
        db_table = "Comment"
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
        ordering = ["-created_at"]

    def __str__(self):
        return self.text
