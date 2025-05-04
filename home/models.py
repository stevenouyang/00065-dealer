from django.db import models
from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from modelcluster.models import ClusterableModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class LinkPage(Page):
    max_count = 1

    description = models.TextField(blank=True)
    enable_social_link = models.BooleanField(default=False)
    enable_floating_whatsapp = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        MultiFieldPanel([
            FieldPanel('enable_social_link'),
            FieldPanel('enable_floating_whatsapp'),
        ], heading="Settings"),
        InlinePanel('link_items', label="Link Items"),
    ]

    class Meta:
        verbose_name = "Link Page"


class LinkItem(Orderable):
    TYPE_CHOICES = [
        ('option', 'Option'),
        ('link', 'Link'),
        ('image', 'Image'),
    ]

    page = ParentalKey(LinkPage, related_name='link_items')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='link')
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    link = models.URLField(blank=True)

    image = models.ImageField(upload_to="link_items/images", null=True, blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(1280, 720)],
        format='WEBP',
        options={'quality': 90}
    )

    panels = [
        FieldPanel('type'),
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('link'),
        FieldPanel('image'),
    ]

    class Meta:
        verbose_name = "Link Item"
