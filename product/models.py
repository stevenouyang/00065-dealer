from django.db import models
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey


# Create your models here.
class Product(ClusterableModel):
    pass
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)


class ProductGallery(models.Model):
    pass
    product = ParentalKey(Product, related_name='product_gallery')
    image = models.ImageField(upload_to='products/gallery')
    