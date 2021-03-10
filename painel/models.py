from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    
    class Meta:
        verbose_name='Brand'
        verbose_name_plural='Brands'

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=244, blank=False)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=99999, blank=False, null=False)
    amount = models.IntegerField(blank=False)
    availability = models.BooleanField(default=True)
    primary_image = models.ImageField(upload_to='products/%Y/%m/%d', blank=False, null=True)
    second_image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    third_image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name


