from ..models import Post
from django import template

register = template.Library()


@register.simple_tag
def count_tag():
    c = Post.tags.all().count()
    return c