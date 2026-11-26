from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSistemap(Sitemap):
    changefreq = 'weely'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated