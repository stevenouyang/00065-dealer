from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup


from .models import ContactFormSubmission, FAQ


class ContactFormSubmissionAdmin(SnippetViewSet):
    model = ContactFormSubmission
    menu_label = "Contact Message"
    icon = "form"
    menu_order = 20
    list_display = ("name", "email")

class FAQAdmin(SnippetViewSet):
    model = FAQ
    menu_label = "FAQs"
    icon = "openquote"
    menu_order = 20
    list_display = ("question", "answer")


class ContactSettingAdmin(SnippetViewSetGroup):
    menu_icon = "mail"
    menu_label = "Contact"
    menu_name = "Contact"
    items = (
        ContactFormSubmissionAdmin,
        FAQAdmin
    )


register_snippet(ContactSettingAdmin)
