from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import Slider, LinkBanner, ContentSetting
# Register your models here.

class SliderAdmin(SnippetViewSet):
    model = Slider
    menu_label = "Slider"
    icon = "image"
    menu_order = 22
    list_display = ("title", "is_active")

class LinkBannerAdmin(SnippetViewSet):
    model = LinkBanner
    menu_label = "Link Banner"
    icon = "image"
    menu_order = 22
    list_display = ("title", "is_active")

class ContentAdmin(SnippetViewSet):
    model = ContentSetting
    menu_label = "Content Setting"
    icon = "image"
    menu_order = 24
    list_display = ("id", )

class ContentSettingAdmin(SnippetViewSetGroup):
    menu_icon = "image"
    menu_label = "Content"
    menu_name = "Content"
    items = (
        SliderAdmin,
        LinkBannerAdmin,
        ContentAdmin,
    )

register_snippet(ContentSettingAdmin)