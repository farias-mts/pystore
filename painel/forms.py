from django import forms

from . import models

class formProduct(forms.Form):
    primary_image = forms.ImageField(required=False)
    second_image = forms.ImageField(required=False)
    third_image = forms.ImageField(required=False)
    name = forms.CharField(max_length=244)
    description = forms.Textarea()
    category = forms.ChoiceField(required=True, widget=forms.Select, choices=[(choice.id, choice.name)for choice in models.Category.objects.all()])
    brand = forms.ChoiceField(required=True, widget=forms.Select,choices=[(choice.id, choice.name)for choice in models.Brand.objects.all()])
    price = forms.DecimalField(decimal_places=2, max_digits=11)
    amount = forms.IntegerField()

    class Meta:
        model = models.Product
        fiels=[
                'name', 
                'description',
                'category',
                'brand',
                'price',
                'amount',
                'primary_image',
                'second_image',
                'third_image',
            ]
