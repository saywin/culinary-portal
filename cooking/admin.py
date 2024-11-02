from django.contrib import admin
from django.utils.safestring import mark_safe

from cooking.models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "watched", "is_published", "category", "created_at", "updated_at", "get_photo"]
    list_display_links = ["id", "title"]
    list_editable = ["is_published"]
    readonly_fields = ["watched"]
    list_filter = ["is_published", "category", "created_at"]

    def get_photo(self, obj):
        photo = obj.photo
        if photo:
            print(photo.url)
            return mark_safe(f"<img src='{photo.url}' width=75/>")

    get_photo.short_description = "Мініатюра"
