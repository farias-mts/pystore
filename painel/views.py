from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginProcess, logout as logoutProcess
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect    

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
    return render(request, 'login/products.html')

def logout(request):
    logoutProcess(request)
    return redirect('/painel/login')
