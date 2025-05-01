from django.shortcuts import render, get_object_or_404, redirect
from collections import defaultdict
from news.models import News
from miscpage.models import MiscPage
from .models import Product, ProductGallery, CarSpecCategory, CarSpec, ProductCarSpec
from content.models import Slider, LinkBanner
from .utils import process_blog_content, process_product_content, set_main_images, process_page_content
from globalsetting.models import ContactSetting
import urllib.parse



# Create your views here.
def index(request):
    news_items = News.objects.filter(is_recommended=True, is_approved=True)
    products = Product.objects.all()
    sliders = Slider.objects.all()
    link_banners = LinkBanner.objects.all()

    set_main_images(products)

    context = {"news_items": news_items, "products": products, "sliders": sliders, "link_banners": link_banners,}
    return render(request, "pages/index.html", context)


def product_list(request):
    products = Product.objects.all()

    set_main_images(products)

    context = {"products": products,}
    return render(request, "pages/product_list.html", context)

def product_detail(request, slug):
    max_width = 800
    max_height = 600
    quality = 90

    product_item = get_object_or_404(Product, slug=slug)
    product_galleries = ProductGallery.objects.filter(product=product_item)
    product_color_variants = product_item.product_color_variants.all()

    process_product_content(product_item.overview, max_width, max_height, quality)

    # Group ProductCarSpec by CarSpecCategory
    car_spec_map = defaultdict(list)
    product_specs = product_item.product_car_specs.select_related('carspec__carspec_category')

    for spec in product_specs:
        category = spec.carspec.carspec_category
        car_spec_map[category].append({
            'title': spec.carspec.title,
            'icon': spec.carspec.icon,
            'value': spec.value
        })

    context = {
        "product_item": product_item,
        "product_galleries": product_galleries,
        "car_specs_by_category": dict(car_spec_map),
        "product_color_variants": product_color_variants,
    }

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
    max_width = 800
    max_height = 600
    quality = 90

    slug_variable = slug
    page_item = get_object_or_404(MiscPage, slug=slug_variable)
    process_page_content(page_item.content, max_width, max_height, quality)


    context = {'page_item': page_item}

    return render(request, "pages/dynamic_page.html", context)

def whatsapp(request):
    contact_setting = ContactSetting.load(request_or_site=request)
    wa_link = contact_setting.whatsapp_link

    product_id = request.GET.get("product_id")
    product = Product.objects.filter(id=int(product_id)).first() if product_id else None

    if product:
        message = f"Halo Denza Indonesia, saya tertarik dengan produk “{product.title}”"
    else:
        message = "Halo Denza Indonesia"

    encoded_message = urllib.parse.quote(message)

    if wa_link:
        final_link = f"{wa_link}&text={encoded_message}"
    else:
        final_link = "/"

    return redirect(final_link)
