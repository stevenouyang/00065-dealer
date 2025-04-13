from django.db import models
from wagtail.admin.panels import FieldPanel
from news.models import News

# admin:
class WhatsappLog(models.Model):
    ip = models.CharField(max_length=500, blank=True, null=True)
    user_agent = models.CharField(max_length=1000, blank=True, null=True)
    preferred_language = models.CharField(max_length=250, blank=True, null=True)
    referer = models.CharField(max_length=1000, blank=True, null=True)
    whatsapp_url = models.URLField(max_length=1000)

    # date
    created_at = models.DateTimeField(auto_now_add=True)

    panels = [
        FieldPanel("ip"),
        FieldPanel("user_agent"),
        FieldPanel("preferred_language"),
        FieldPanel("referer"),
        FieldPanel("whatsapp_url"),
    ]

    def __str__(self):
        return self.ip


# admin:
class NewsVisitLog(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    ip = models.CharField(max_length=1000, blank=True, null=True)
    user_agent = models.CharField(max_length=1000, blank=True, null=True)
    preferred_language = models.CharField(max_length=1000, blank=True, null=True)
    referer = models.CharField(max_length=1000, blank=True, null=True)

    # date
    created_at = models.DateTimeField(auto_now_add=True)

    panels = [
        FieldPanel("news"),
        FieldPanel("ip"),
        FieldPanel("user_agent"),
        FieldPanel("preferred_language"),
        FieldPanel("referer"),
    ]

    def __str__(self):
        return self.ip



# admin:
class PageVisitLog(models.Model):
    url = models.URLField()
    type = models.CharField(
        max_length=50, blank=True, null=True
    )  # INDEX / BLOG_LIST / PORTFOLIO_LIST
    ip = models.CharField(max_length=50, blank=True, null=True)
    user_agent = models.CharField(max_length=1000, blank=True, null=True)
    preferred_language = models.CharField(max_length=1000, blank=True, null=True)
    referer = models.CharField(max_length=1000, blank=True, null=True)

    # date
    created_at = models.DateTimeField(auto_now_add=True)

    panels = [
        FieldPanel("url"),
        FieldPanel("type"),
        FieldPanel("ip"),
        FieldPanel("user_agent"),
        FieldPanel("preferred_language"),
        FieldPanel("referer"),
    ]

    def __str__(self):
        return self.ip
