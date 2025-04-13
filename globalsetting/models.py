from django.db import models
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

@register_setting
class ContactSetting(BaseGenericSetting):
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    whatsapp_link = models.URLField(blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)

    panels = [
        FieldPanel("whatsapp_number"),
        FieldPanel("whatsapp_link"),
        FieldPanel("email"),
    ]


@register_setting
class SocialSetting(BaseGenericSetting):
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    tiktok_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    telegram_link = models.URLField(blank=True, null=True)

    panels = [
        FieldPanel("instagram_link"),
        FieldPanel("linkedin_link"),
        FieldPanel("tiktok_link"),
        FieldPanel("facebook_link"),
        FieldPanel("twitter_link"),
        FieldPanel("youtube_link"),
        FieldPanel("telegram_link"),
    ]


@register_setting
class PageSEOSetting(BaseGenericSetting):
    home_meta_key = models.TextField(max_length=100, blank=True, null=True)
    home_meta_desc = models.TextField(max_length=160, blank=True, null=True)
    blog_meta_key = models.TextField(max_length=100, blank=True, null=True)
    blog_meta_desc = models.TextField(max_length=160, blank=True, null=True)
    product_meta_key = models.TextField(max_length=100, blank=True, null=True)
    product_meta_desc = models.TextField(max_length=160, blank=True, null=True)

    panels = [
        FieldPanel("home_meta_key"),
        FieldPanel("home_meta_desc"),
        FieldPanel("blog_meta_key"),
        FieldPanel("blog_meta_desc"),
        FieldPanel("product_meta_key"),
        FieldPanel("product_meta_desc"),
    ]

@register_setting
class FeaturesFlag(BaseGenericSetting):
    module_news = models.BooleanField(default=True)

    panels = [
        FieldPanel("module_news"),
    ]