from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer

# Create your views here.

## Detail-api-view
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

##List-api-view
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


