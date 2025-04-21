from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import MiscPage

class MiscPageAdmin(SnippetViewSet):
    model = MiscPage
    menu_label = "Misc Page"
    icon = "draft"
    menu_order = 20
    list_display = ("title", "is_show", "show_in_footer")

class PageSettingAdmin(SnippetViewSetGroup):
    menu_icon = "doc-empty"
    menu_label = "Page"
    menu_name = "Page"
    items = (
        MiscPageAdmin,
    )

register_snippet(PageSettingAdmin)