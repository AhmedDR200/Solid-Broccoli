from django.shortcuts import render
from django.http import JsonResponse
from product.models import Product 


def api_home(request, *args, **kwargs):
    model = Product.objects.all().order_by("?").first()
    data = {}
    if model:
        data["id"] = model.id 
        data["title"] = model.title
        data['content'] = model.content
        data['price'] = model.price

    return JsonResponse(data)
