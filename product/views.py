from django.shortcuts import render, get_object_or_404
from news.models import News
from .models import Product, ProductGallery
from content.models import Slider
from .utils import process_blog_content, set_main_images



# Create your views here.
def index(request):
    news_items = News.objects.filter(is_recommended=True, is_approved=True)
    products = Product.objects.all()
    sliders = Slider.objects.all()

    set_main_images(products)

    context = {"news_items": news_items, "products": products, "sliders": sliders}
    return render(request, "pages/index.html", context)


def product_list(request):
    products = Product.objects.all()

    set_main_images(products)

    context = {"products": products,}
    return render(request, "pages/product_list.html", context)


def product_detail(request, slug):
    product_item = get_object_or_404(Product, slug=slug)

    context = {'product_item': product_item}
    return render(request, "pages/product_detail.html", context)


def news_list(request):
    news_items = News.objects.filter(is_approved=True)

    context = {"news_items": news_items, }

    return render(request, "pages/news_list.html", context)


def news_detail(request, slug):
    max_width = 800
    max_height = 600
    quality = 90

    news_item = get_object_or_404(News, slug=slug)

    process_blog_content(news_item.content, max_width, max_height, quality)

    context = {"news_item": news_item}
    return render(request, "pages/news_detail.html", context)


def static_contact_us(request):
    context = {}
    return render(request, "pages/static_contact.html", context)


def dynamic_page(request, slug):
    slug_variable = slug
    context = {}
    return render(request, "pages/dynamic_page.html", context)
