from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from product.models import Product 
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializers import ProductSerializer
from rest_framework import generics


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    model = Product.objects.all().order_by("?").first()
    data = {}
    if model:
        # data["id"] = model.id 
        # data["title"] = model.title
        # data['content'] = model.content
        # data['price'] = model.price
        # data = model_to_dict(model, fields=("id","title","price","sale_price"))
          data = ProductSerializer(model).data
    return Response(data)


@api_view(['POST'])
def api_home_post(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
         data = serializer.save()
         print(serializer.data)
    return Response(serializer.data)



