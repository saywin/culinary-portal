from django import template
from cooking.models import Category
from django.db.models import Count

register = template.Library()


@register.simple_tag()
def get_all_categories():
    """Кнопки категорій"""
    return Category.objects.annotate(cnt=Count("posts")).filter(posts__is_published=True).filter(cnt__gt=0)
