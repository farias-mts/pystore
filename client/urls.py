from django.urls import path

from . import views

urlpatterns = [
    path('' ,views.index),
    path('product', views.viewProducts, name='viewProducts'),
    path('teste', views.teste),
    path('product/get', views.getProducts, name='getProducts')
]