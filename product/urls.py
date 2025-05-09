from django.urls import path
from . import views
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *
from django.views.generic import TemplateView

app_name = 'core'

sitemaps = {
    'static': StaticViewSitemap,
    'product' : ProductSitemap,
    'blog' : NewsSitemap,
    'page' : PageSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),
    path('produk/', views.product_list, name='product_list'),
    path('produk/<slug:slug>/', views.product_detail, name='product_detail'),
    path('berita/', views.news_list, name='news_list'),
    path('berita/<slug:slug>/', views.news_detail, name='news_detail'),
    path('hubungi-kami/', views.static_contact_us, name='static_contact_us'),
    path('halaman/<slug:slug>/', views.dynamic_page, name='dynamic_page'),
    path('whatsapp/', views.whatsapp, name='whatsapp'),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name='robots'),
]


