from django.db import models
from wagtail.admin.panels import FieldPanel

# Create your models here.
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
    image = models.ImageField(upload_to="slider_images")

    panels = [
        FieldPanel("title"),
        FieldPanel("theme"),
        FieldPanel("description"),
        FieldPanel("cta_button"),
        FieldPanel("cta_text"),
        FieldPanel("cta_link"),
        FieldPanel("image"),
    ]

    def __str__(self):
        return self.title