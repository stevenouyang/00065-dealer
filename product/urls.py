from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('contact-us/', views.static_contact_us, name='static_contact_us'),
    path('<slug:slug>/', views.dynamic_page, name='dynamic_page'),
]
