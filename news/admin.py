from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import NewsCategory, News

class NewsCategoryAdmin(SnippetViewSet):
    model = NewsCategory
    menu_label = "News Category"
    icon = "doc-empty"
    menu_order = 20
    list_display = ("title", )

class NewsAdmin(SnippetViewSet):
    model = News
    menu_label = "News"
    icon = "list-ul"
    menu_order = 20
    list_display = ("title", "category", "is_approved", "is_recommended")

class NewsSettingAdmin(SnippetViewSetGroup):
    menu_icon = "doc-full"
    menu_label = "News"
    menu_name = "News"
    items = (
        NewsCategoryAdmin,
        NewsAdmin
    )

register_snippet(NewsSettingAdmin)