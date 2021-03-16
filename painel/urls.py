from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('login/', views.login),
    path('', views.index),
    path('logout/', views.logout),
    path('products/', views.newProduct),
    path('category/', views.newCategory),
    path('brand/', views.newBrand),
    path('user/', views.newUser),
    path('products/search', views.getProducts, name='search'),
    path('products/<id>', views.editProduct),
    path('products/<id>/delete/', views.deleteProduct),
    path('teste/', views.teste)
] 