from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('login/', views.login),
    path('', views.index),
    path('logout/', views.logout),
    path('products/', views.newProduct),
    path('teste/', views.teste)
] 