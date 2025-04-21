from django.db import models
from django.urls import reverse
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from autoslug import AutoSlugField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Adjust
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks
from django.db.models.signals import pre_save
from django.dispatch import receiver
import math
import uuid
import os
from bs4 import BeautifulSoup

class MiscPage(index.Indexed, models.Model):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from="title", blank=True, null=True)

    is_show = models.BooleanField(default=False)
    show_in_footer = models.BooleanField(default=False)

    image = models.ImageField(upload_to="miscpage", null=True, default=None)
    image_processed = ImageSpecField(
        source="image",
        processors=[ResizeToFill(1400, 800)],
        format="webP",
        options={"quality": 90},
    )

    content = StreamField(
        [
            (
                "paragraph",
                blocks.RichTextBlock(features=["p", "a"]),
            ),
            (
                "h4",
                blocks.CharBlock(features=["h4"]),
            ),
            (
                "h6",
                blocks.CharBlock(features=["h6"]),
            ),
            (
                "ordered_list",
                blocks.RichTextBlock(
                    features=["ol"],
                ),
            ),
            (
                "unordered_list",
                blocks.RichTextBlock(
                    features=["ul"],
                ),
            ),
            ("blockquote_1", blocks.CharBlock()),
            (
                "image",
                ImageChooserBlock(label="Image", help_text="800 x 600"),
            ),
        ],
        use_json_field=True,
        null=True,
        blank=True,
    )

    # seo
    meta_key = models.TextField(max_length=100, blank=True, null=True)
    meta_desc = models.TextField(max_length=160, blank=True, null=True)

    # date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    panels = [
        FieldPanel("title"),
        FieldPanel("is_show"),
        FieldPanel("show_in_footer"),
        FieldPanel("image"),
        FieldPanel("content"),
        FieldPanel("meta_key"),
        FieldPanel("meta_desc"),
    ]

    def __str__(self):
        return self.title

