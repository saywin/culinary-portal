# Generated by Django 5.1.2 on 2024-11-10 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cooking", "0003_alter_post_category_alter_post_is_published_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Коментарі",
                "verbose_name_plural": "Коментар",
            },
        ),
        migrations.AlterModelTable(
            name="comment",
            table="Comment",
        ),
    ]