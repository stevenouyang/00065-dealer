from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "pages/index.html", context)


def product_list(request, slug):
    slug_variable = slug
    context = {}
    return render(request, "pages/product_list.html", context)


def product_detail(request, slug):
    slug_variable = slug
    context = {}
    return render(request, "pages/product_detail.html", context)


def news_list(request, slug):
    slug_variable = slug
    context = {}
    return render(request, "pages/news_list.html", context)


def news_detail(request, slug):
    slug_variable = slug
    context = {}
    return render(request, "pages/news_detail.html", context)


def static_contact_us(request):
    context = {}
    return render(request, "pages/static_contact.html", context)


def dynamic_page(request, slug):
    slug_variable = slug
    context = {}
    return render(request, "pages/dynamic_page.html", context)
