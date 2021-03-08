from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

class Brand(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    
    class Meta:
        verbose_name='Brand'
        verbose_name_plural='Brands'

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=244, blank=False)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=99999, blank=False)
    amount = models.IntegerField(blank=False)
    availability = models.BooleanField(default=True)
    primary_image = models.ImageField(upload_to=, blank=False, null=True)
    second_image = models.ImageField(upload_to=, blank=True, null=True)
    third_image = models.ImageField(upload_to=, blank=True, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


