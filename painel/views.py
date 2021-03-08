from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect    

# Create your views here.

def login(request):
    if request.method == 'POST':
        print(request.POST['username'])
        print(request.POST['password'])
    return render(request, 'login/login.html')

@login_required(login_url='login/')
def index(request):
    return HttpResponse('Logado')
