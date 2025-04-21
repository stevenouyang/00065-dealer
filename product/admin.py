from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import Product, CarSpecCategory, CarSpec

class ProductAdmin(SnippetViewSet):
    model = Product
    menu_label = "Product"
    icon = "pick"
    menu_order = 20
    list_display = ("title", "is_coming_soon", )

class CarSpecAdmin(SnippetViewSet):
    model = CarSpec
    menu_label = "Car Specifications"
    icon = "sliders"
    menu_order = 20
    list_display = ("title", "carspec_category", )

class CarSpecCategoryAdmin(SnippetViewSet):
    model = CarSpecCategory
    menu_label = "Car Spec Category"
    icon = "list-ul"
    menu_order = 20
    list_display = ("title", )

class ProductSettingAdmin(SnippetViewSetGroup):
    menu_icon = "pick"
    menu_label = "Product"
    menu_name = "Product"
    items = (
        ProductAdmin,
        CarSpecAdmin,
        CarSpecCategoryAdmin
    )

register_snippet(ProductSettingAdmin)