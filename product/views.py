from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# Create your views here.


class ProductDetail(generics.RetrieveAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
    #  lookup field = "pk"