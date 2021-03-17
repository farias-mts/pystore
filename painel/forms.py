from django import forms

from . import models

class formProduct(forms.ModelForm):
    category = forms.ModelChoiceField(required=True, widget=forms.Select, queryset=models.Category.objects.all())
    brand = forms.ModelChoiceField(required=True, widget=forms.Select, queryset=models.Brand.objects.all())

    class Meta:
        model = models.Product
        fields=[
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

