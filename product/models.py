from django.db import models
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel


# Create your models here.
class Product(ClusterableModel):
    pass
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)


class ProductGallery(models.Model):
    pass
    product = ParentalKey(Product, related_name='product_gallery')
    image = models.ImageField(upload_to='products/gallery')


class CarSpecCategory(models.Model):
    title = models.CharField(max_length=255)

    panels = [
        FieldPanel("title"),
    ]

    def __str__(self):
        return self.title


class CarSpec(models.Model):
    carspec_category = models.ForeignKey(CarSpecCategory, on_delete=models.CASCADE, related_name="car_specs")
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    panels = [
        FieldPanel("carspec_category"),
        FieldPanel("title"),
        FieldPanel("icon"),
    ]

    def __str__(self):
        return self.title


class ProductCarSpec(models.Model):
    product = ParentalKey(Product, related_name='product_car_specs', on_delete=models.CASCADE)
    carspec = models.ForeignKey(CarSpec, related_name='product_car_specs', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    panels = [
        FieldPanel("product"),
        FieldPanel("carspec"),
        FieldPanel("value"),
    ]

    def __str__(self):
        return f"{self.product.title} - {self.carspec.title}: {self.value}"

