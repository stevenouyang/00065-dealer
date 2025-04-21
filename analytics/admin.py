from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import WhatsappLog, NewsVisitLog, PageVisitLog
# Register your models here.

class WhatsappLogAdmin(SnippetViewSet):
    model = WhatsappLog
    menu_label = "Whatsapp Log"
    icon = "success"
    menu_order = 21
    list_display = ("whatsapp_url" ,"ip")

class NewsVisitLogAdmin(SnippetViewSet):
    model = NewsVisitLog
    menu_label = "News Visit Log"
    icon = "resubmit"
    menu_order = 21
    list_display = ("news", "ip")

class PageVisitLogAdmin(SnippetViewSet):
    model = PageVisitLog
    menu_label = "Page Visit Log"
    icon = "resubmit"
    menu_order = 21
    list_display = ("url", "type", "ip")

class AnalyticsSettingAdmin(SnippetViewSetGroup):
    menu_icon = "plus"
    menu_label = "Analytics"
    menu_name = "Analytics"
    items = (
        WhatsappLogAdmin,
        NewsVisitLogAdmin,
        PageVisitLogAdmin
    )

register_snippet(AnalyticsSettingAdmin)