from django import forms

from . import models

class formProduct(forms.Form):
    primary_image = forms.ImageField()
    second_image = forms.ImageField()
    second_image = forms.ImageField()
    name = forms.CharField(max_length=244)
    slug = forms.SlugField()
    description = forms.Textarea()
    category = forms.ChoiceField(choices=models.Category.objects.all())
    brad = forms.ChoiceField(choices=models.Brand.objects.all())
    price = forms.DecimalField(decimal_places=2, max_digits=11)
    amount = forms.IntegerField()
    availability = forms.BooleanField()

    class Meta:
        model = models.Product
        fiels=[
                'name', 
                'slug', 
                'description',
                'category',
                'brad',
                'price',
                'amount',
                'availability'
            ]
