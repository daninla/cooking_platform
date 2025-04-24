from django import template
from cooking.models import Category
from django.db.models import Count

register = template.Library()

@register.simple_tag()
def get_all_categories():
    """Кнопки категорий"""
    return Category.objects.annotate(cnt=Count('post')).filter(cnt__gt=0)

