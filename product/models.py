from django.db import models
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index


# Create your models here.
class Product(index.Indexed, ClusterableModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    is_coming_soon = models.BooleanField(default=False)
    is_color_variant = models.BooleanField(default=False)
    overview = StreamField(
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
    youtube_embed = models.TextField(blank=True, null=True)
    image_dimension = models.ImageField(upload_to="product/dimension", blank=True, null=True)
    pdf_catalogue = models.FileField(upload_to='products/pdf_catalogues', blank=True, null=True)

    highlight_battery = models.CharField(max_length=255, blank=True, null=True)
    highlight_seat = models.CharField(max_length=255, blank=True, null=True)
    highlight_range = models.CharField(max_length=255, blank=True, null=True)
    highlight_power = models.CharField(max_length=255, blank=True, null=True)
    highlight_acceleration = models.CharField(max_length=255, blank=True, null=True)

    panels = [
        FieldPanel("title"),

        FieldPanel("is_coming_soon"),
        FieldPanel("is_color_variant"),
        FieldPanel("overview"),
        FieldPanel("youtube_embed"),
        FieldPanel("image_dimension"),
        FieldPanel("pdf_catalogue"),

        FieldPanel("highlight_battery"),
        FieldPanel("highlight_seat"),
        FieldPanel("highlight_range"),
        FieldPanel("highlight_power"),
        FieldPanel("highlight_acceleration"),

        InlinePanel("product_color_variants"),
        InlinePanel("product_gallery"),
        InlinePanel("product_car_specs"),
    ]

    search_fields = [
        index.SearchField("title"),
    ]

    def __str__(self):
        return self.title


# inline
class ProductGallery(models.Model):
    product = ParentalKey(Product, related_name='product_gallery')
    image = models.ImageField(upload_to='products/gallery')


# inline
class ProductColorVariant(models.Model):
    product = ParentalKey(Product, related_name='product_color_variants', on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
    color_hex = models.CharField(max_length=6)
    image = models.ImageField(upload_to='products/color_variants')


class CarSpecCategory(index.Indexed, models.Model):
    title = models.CharField(max_length=255)

    panels = [
        FieldPanel("title"),
    ]

    search_fields = [
        index.SearchField("title"),
    ]


    def __str__(self):
        return self.title


class CarSpec(index.Indexed, models.Model):
    title = models.CharField(max_length=255)
    carspec_category = models.ForeignKey(CarSpecCategory, on_delete=models.CASCADE, related_name="car_specs_category")
    icon = models.CharField(max_length=255)

    panels = [
        FieldPanel("carspec_category"),
        FieldPanel("title"),
        FieldPanel("icon"),
    ]

    search_fields = [
        index.SearchField("title"),
    ]

    def __str__(self):
        return self.title


# inline
class ProductCarSpec(models.Model):
    product = ParentalKey(Product, related_name='product_car_specs', on_delete=models.CASCADE)
    carspec = models.ForeignKey(CarSpec, related_name='spec_car_specs', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)