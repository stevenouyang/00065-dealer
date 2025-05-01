from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('produk/', views.product_list, name='product_list'),
    path('produk/<slug:slug>/', views.product_detail, name='product_detail'),
    path('berita/', views.news_list, name='news_list'),
    path('berita/<slug:slug>/', views.news_detail, name='news_detail'),
    path('hubungi-kami/', views.static_contact_us, name='static_contact_us'),
    path('halaman/<slug:slug>/', views.dynamic_page, name='dynamic_page'),
    path('whatsapp/', views.whatsapp, name='whatsapp'),
]


