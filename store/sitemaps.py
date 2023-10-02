from django.contrib.sitemaps import Sitemap
from .models import Post,Category,Store


class StoreSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Store.objects.all()

    # def lastmod(self, store):
    #     return store.article_published

    def location(self, obj):
        return '/store/%s' % (obj.slug)