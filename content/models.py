from django.db import models
from wagtail.admin.panels import FieldPanel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Adjust

# Create your models here.
class LinkBanner(models.Model):
    title = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    cta_text = models.CharField(max_length=60)
    cta_link = models.URLField(max_length=255)
    cta_blank = models.BooleanField(default=False)
    image = models.ImageField(upload_to="link_banners")
    image_processed = ImageSpecField(
        source="image",
        processors=[ResizeToFill(600, 400)],
        format="webP",
        options={"quality": 90},
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("is_active"),
        FieldPanel("cta_text"),
        FieldPanel("cta_link"),
        FieldPanel("cta_blank"),
        FieldPanel("image"),
    ]

    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=255)
    theme = models.CharField(
        max_length=10,
        choices=(("DARK", "Dark"), ("LIGHT", "Light")),
        default="DARK"
    )
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    cta_button = models.BooleanField(default=True)
    cta_text = models.CharField(max_length=255, blank=True, null=True)
    cta_link = models.URLField(max_length=255, blank=True, null=True)
    cta_blank = models.BooleanField(default=False)
    image = models.ImageField(upload_to="slider_images")
    image_processed = ImageSpecField(
        source="image",
        processors=[ResizeToFill(1920, 1080)],
        format="webP",
        options={"quality": 90},
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("theme"),
        FieldPanel("is_active"),
        FieldPanel("description"),
        FieldPanel("cta_button"),
        FieldPanel("cta_text"),
        FieldPanel("cta_link"),
        FieldPanel("cta_blank"),
        FieldPanel("image"),
    ]

    def __str__(self):
        return self.title