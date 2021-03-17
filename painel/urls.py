from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('login/', views.login),
    path('', views.index),
    path('logout/', views.logout),
    path('products/', views.newProduct),
    path('category/', views.newCategory),
    path('category/search', views.queryCategory, name='searchCategory'),
    path('category/<id>/delete', views.deleteCategory, name='deleteCategory'),
    path('brand/', views.newBrand),
    path('brand/search', views.queryBrand, name='searchBrand'),
    path('brand/<id>/delete', views.deleteBrand, name='deleteBrand'),
    path('user/', views.newUser),
    path('products/search', views.getProducts, name='search'),
    path('products/<id>', views.editProduct),
    path('products/<id>/delete/', views.deleteProduct),
    path('products/<id>/update/', views.updateProduct, name='updateProduct'),
    path('teste/', views.teste)
] 