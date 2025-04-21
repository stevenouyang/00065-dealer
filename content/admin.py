from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import Slider
# Register your models here.

class SliderAdmin(SnippetViewSet):
    model = Slider
    menu_label = "Slider"
    icon = "image"
    menu_order = 22
    list_display = ("title", "is_active")

class ContentSettingAdmin(SnippetViewSetGroup):
    menu_icon = "image"
    menu_label = "Content"
    menu_name = "Content"
    items = (
        SliderAdmin,
    )

register_snippet(ContentSettingAdmin)