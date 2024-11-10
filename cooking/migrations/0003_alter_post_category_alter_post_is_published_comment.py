# Generated by Django 5.1.2 on 2024-11-10 16:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cooking", "0002_alter_category_options_alter_post_options_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="cooking.category",
                verbose_name="Категорія",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Опубліковано?"),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Коментар")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата створення"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата оновлення"),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="cooking.post",
                        verbose_name="Стаття",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Користувач",
                    ),
                ),
            ],
            options={
                "verbose_name": "",
                "verbose_name_plural": "",
                "db_table": "",
                "ordering": ["-created_at"],
            },
        ),
    ]