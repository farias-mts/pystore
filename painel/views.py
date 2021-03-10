from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginProcess, logout as logoutProcess
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect  

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
    if request.method=='POST':
            print(request.POST['name'])
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
                primary_image=primary_image,
                second_image=second_image,
                third_image=third_image
            )
            new_product.save()
            print('Produto criado')
    context = {
        'formProduct':formProduct,
    }
    return render(request, 'login/products.html', context)

def teste(request):
    return render(request, 'teste.html')
