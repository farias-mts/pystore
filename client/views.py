from django.shortcuts import render

# Create your views here.
from painel.models import Category, Brand

def index(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'base.html', context)

def teste(request):
    return render(request, 'pieces/slide.html')

