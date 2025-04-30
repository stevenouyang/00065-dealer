from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Adjust
from solo.models import SingletonModel

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

class BrandingSetting(SingletonModel):
    pass

class ContentSetting(SingletonModel):
    product_page_image = models.ImageField(upload_to='products/', blank=True, null=True)
    product_page_image_processed = ImageSpecField(
        source="product_page_image",
        processors=[ResizeToFill(1920, 600)],
        format="webP",
        options={"quality": 90},
    )

    footer_image = models.ImageField(upload_to='footer/', blank=True, null=True)
    footer_image_processed = ImageSpecField(
        source="product_page_image",
        processors=[ResizeToFill(1920, 1080)],
        format="webP",
        options={"quality": 90},
    )
    footer_description = models.CharField(max_length=140, blank=True, null=True)

    bottom_cta_1_title = models.CharField(max_length=40, blank=True, null=True)
    bottom_cta_1_image = models.ImageField(upload_to='cta/', blank=True, null=True)
    bottom_cta_1_image_processed = ImageSpecField(
        source="bottom_cta_1_image",
        processors=[ResizeToFill(600, 400)],
        format="webP",
        options={"quality": 90},
    )
    bottom_cta_1_desc = models.CharField(max_length=100, blank=True, null=True)
    bottom_cta_1_button_text = models.CharField(max_length=20, blank=True, null=True)
    bottom_cta_1_icon = models.CharField(max_length=20, blank=True, null=True)
    bottom_cta_1_button_link = models.URLField(blank=True, null=True)
    bottom_cta_1_new_tab = models.BooleanField(default=False)

    bottom_cta_2_title = models.CharField(max_length=40, blank=True, null=True)
    bottom_cta_2_image = models.ImageField(upload_to='cta/', blank=True, null=True)
    bottom_cta_2_image_processed = ImageSpecField(
        source="bottom_cta_2_image",
        processors=[ResizeToFill(600, 400)],
        format="webP",
        options={"quality": 90},
    )
    bottom_cta_2_desc = models.CharField(max_length=100, blank=True, null=True)
    bottom_cta_2_button_text = models.CharField(max_length=20, blank=True, null=True)
    bottom_cta_2_icon = models.CharField(max_length=20, blank=True, null=True)
    bottom_cta_2_button_link = models.URLField(blank=True, null=True)
    bottom_cta_2_new_tab = models.BooleanField(default=False)

    product_highlight_image = models.ImageField(upload_to='highlights/', blank=True, null=True)
    product_highlight_image_processed = ImageSpecField(
        source="product_highlight_image",
        format="webP",
        options={"quality": 90},
    )
    product_highlight_title_1 = models.CharField(max_length=20, blank=True, null=True)
    product_highlight_title_2 = models.CharField(max_length=20, blank=True, null=True)
    product_highlight_desc = models.CharField(max_length=255, blank=True, null=True)

    product_detail_image = models.ImageField(upload_to='details/', blank=True, null=True)
    product_detail_image_processed = ImageSpecField(
        source="product_detail_image",
        format="webP",
        options={"quality": 90},
    )
    product_detail_desc = models.CharField(max_length=500, blank=True, null=True)
    product_detail_button_text = models.CharField(max_length=20, blank=True, null=True)
    product_detail_button_link = models.URLField(blank=True, null=True)
    product_detail_new_tab = models.BooleanField(default=False)

    product_detail_icon_1 = models.CharField(max_length=20, blank=True, null=True)
    product_detail_title_1 = models.CharField(max_length=30, blank=True, null=True)
    product_detail_desc_1 = models.CharField(max_length=80, blank=True, null=True)
    product_detail_icon_2 = models.CharField(max_length=20, blank=True, null=True)
    product_detail_title_2 = models.CharField(max_length=30, blank=True, null=True)
    product_detail_desc_2 = models.CharField(max_length=80, blank=True, null=True)
    product_detail_icon_3 = models.CharField(max_length=20, blank=True, null=True)
    product_detail_title_3 = models.CharField(max_length=30, blank=True, null=True)
    product_detail_desc_3 = models.CharField(max_length=80, blank=True, null=True)


    panels = [
        FieldPanel("product_page_image"),

        MultiFieldPanel([
            FieldPanel("footer_image"),
            FieldPanel("footer_description"),
        ], heading="Footer"),

        MultiFieldPanel([
            FieldPanel("bottom_cta_1_title"),
            FieldPanel("bottom_cta_1_image"),
            FieldPanel("bottom_cta_1_desc"),
            FieldPanel("bottom_cta_1_button_text"),
            FieldPanel("bottom_cta_1_icon"),
            FieldPanel("bottom_cta_1_button_link"),
            FieldPanel("bottom_cta_1_new_tab"),
        ], heading="Bottom CTA 1"),

        MultiFieldPanel([
            FieldPanel("bottom_cta_2_title"),
            FieldPanel("bottom_cta_2_image"),
            FieldPanel("bottom_cta_2_desc"),
            FieldPanel("bottom_cta_2_button_text"),
            FieldPanel("bottom_cta_2_icon"),
            FieldPanel("bottom_cta_2_button_link"),
            FieldPanel("bottom_cta_2_new_tab"),
        ], heading="Bottom CTA 2"),

        MultiFieldPanel([
            FieldPanel("product_highlight_image"),
            FieldPanel("product_highlight_title_1"),
            FieldPanel("product_highlight_title_2"),
            FieldPanel("product_highlight_desc"),
        ], heading="Product Highlight"),

        MultiFieldPanel([
            FieldPanel("product_detail_image"),
            FieldPanel("product_detail_desc"),
            FieldPanel("product_detail_button_text"),
            FieldPanel("product_detail_button_link"),
            FieldPanel("product_detail_new_tab"),
            FieldPanel("product_detail_icon_1"),
            FieldPanel("product_detail_title_1"),
            FieldPanel("product_detail_desc_1"),
            FieldPanel("product_detail_icon_2"),
            FieldPanel("product_detail_title_2"),
            FieldPanel("product_detail_desc_2"),
            FieldPanel("product_detail_icon_3"),
            FieldPanel("product_detail_title_3"),
            FieldPanel("product_detail_desc_3"),
        ], heading="Product Detail"),
    ]

    def __str__(self):
        return f"Product Page {self.id}"