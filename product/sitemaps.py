from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from miscpage.models import MiscPage
from product.models import Product
from news.models import News


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return [
            'core:index',
            'core:product_list',
            'core:news_list',
            'core:static_contact_us',
        ]

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    def items(self):
        return Product.objects.all()

class NewsSitemap(Sitemap):
    def items(self):
        return News.objects.all()

class PageSitemap(Sitemap):
    def items(self):
        return MiscPage.objects.all()

