from django.shortcuts import render

# Create your views here.
from painel.models import Category, Brand, Product

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories':categories,
        'products':products,
    }
    return render(request, 'index.html', context)

def teste(request):
    return render(request, 'pieces/slide.html')

