from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.
from painel.models import Category, Brand, Product
import json

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories':categories,
        'products':products,
    }
    return render(request, 'index.html', context)

def viewProducts(request):
    if request.method == 'POST':
        category = str(request.POST['category']).replace('"', '')
        maxPrice = minPrice = 0
        avability = False
        products = Product.objects.all()
        brands=[]
        for product in products:
            if str(product.category) == category:
                if product.brand not in brands:
                    brands.append(product.brand)
        for product in products:
            if category == str(product.category):
                if product.availability > 0:
                    avability = True
                if product.price >= maxPrice:
                    maxPrice = product.price
                elif product.price < minPrice:
                    minPrice = product.price
                else:
                    minPrice = product.price
    context = {
        'maxPrice':maxPrice,
        'minPrice':minPrice,
        'avability':avability,
        'brands':brands,
        'category':category,
    }
    return render(request, 'products/products.html', context)

@csrf_exempt
def getProducts(request):
    products = Product.objects.all()
    filter_products=[]
    if request.method == 'POST':
        brands =json.loads(request.POST['brand'])
        min_price = request.POST['minPrice']
        max_price = request.POST['maxPrice']
        for product in products:
            for brand in brands:
                if str(product.brand) == str(brand):
                    if float(product.price)>=float(min_price) and float(product.price)<=float(max_price):
                        filter_products.append(product) 
        products = filter_products
    elif request.method == 'GET':
        category = str(request.GET['category']).replace('"', '')
        filter_products = [product for product in products if category == str(product.category)]

    context = {
        'products':filter_products,
    }
    return render(request, 'products/cardProduct.html', context)

def showProduct(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product':product
    }
    return render(request, 'products/showProduct.html', context)

def teste(request):
    return render(request, 'pieces/slide.html')

