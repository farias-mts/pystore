from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginProcess, logout as logoutProcess
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect  
from django.contrib.auth.models import User

from . import forms
from . import models

# Create your views here.

@csrf_protect
def login(request):
    error = False
    if request.method == 'POST':
        user = authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
        if user is not None:
            loginProcess(request, user)
            return redirect('/painel/')
        else:
            error = True
    context ={
        'error':error
    }
    return render(request, 'login/login.html', context)

@login_required(login_url='login/')
def index(request):
    return render(request, 'panel.html')

def logout(request):
    logoutProcess(request)
    return redirect('/painel/login')

@csrf_protect
@login_required(login_url='login/')
def newProduct(request):
    formProduct = forms.formProduct()
    formSearch = forms.formSearch()
    if request.method=='POST':
            primary_image = request.POST['primary_image']
            second_image = request.POST['second_image']
            third_image = request.POST['third_image']
            name = request.POST['name']
            description = request.POST['description']
            category = models.Category.objects.get(id=request.POST['category'])
            brand = models.Brand.objects.get(id=request.POST['brand'])
            price = request.POST['price']
            amount = request.POST['amount']
            new_product = models.Product(
                name=name,
                description=description,
                category=category,
                brand=brand,
                price=price,
                amount=amount,
                primary_image= primary_image,
                second_image=second_image,
                third_image=third_image
            )
            new_product.save()
            print('Produto criado')
    context = {
        'formProduct':formProduct,
        'formSearch':formSearch
    }
    return render(request, 'login/products.html', context)

@csrf_protect
@login_required(login_url='login/')
def getProducts(request):
    if request.method == 'POST':
        query = request.POST['search_text']
    else:
        query = ''
    products = models.Product.objects.filter(name__contains=query)
    context = {
        'products':products,
    }
    return render(request, 'login/resultProducts.html', context)

@csrf_protect
@login_required(login_url='login/')
def editProduct(request, id):
    products = models.Product.objects.filter(id=id)
    context = {
        'products':products
    }
    return render(request, 'login/product.html', context)

@csrf_protect
@login_required(login_url='login/')
def deleteProduct(request, id):
    models.Product.objects.filter(id=id).delete()
    return redirect('/painel/products')

@csrf_protect
@login_required(login_url='login/')
def newCategory(request):
    category = models.Category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        new_category = models.Category(
            name=name
        )
        new_category.save()
        print('Categoria Criada')
    context = {
        'category':category
    }
    return render(request, 'login/category.html', context)

@csrf_protect
@login_required(login_url='login/')
def newBrand(request):
    if request.method == 'POST':
        name = request.POST['name']
        new_brand = models.Brand(
            name=name
        )
        new_brand.save()
        print('Fabricante criado')
    return render(request, 'login/brand.html')

def newUser(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        second_name = request.POST['second_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(
            username,
            email,
            password
        )
        user.first_name = first_name
        user.last_name = second_name
        user.save()

    return render(request, 'login/user.html')

def teste(request):
    query = 'C'
    t = models.Category.objects.filter(name__contains=query)
    print(t)
    '''for p in t:
        if query in p.name:
            print(p)'''
