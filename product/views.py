from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.


class ProductDetail(generics.RetrieveAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
    #  lookup field = "pk"


class ProductCreate(generics.CreateAPIView):
     queryset=Product.objects.all()
     serializer_class=ProductSerializer


class ProductList(generics.ListCreateAPIView):
     queryset = Product.objects.all().order_by('id')[:4]
     serializer_class = ProductSerializer



@api_view(['GET','POST'])
def product_alt_view(request,pk=None ,*args, **kwargs):
     method = request.method
     if method == "GET":
          if pk is not None:
               queryset = Product.objects.filter(pk=pk)
               if not queryset.exist():
                    raise Http404
               return Response()
          
          queryset = Product.objects.all()
          data = ProductSerializer(queryset, many=True).data
          return Response(data)
     
     if method == "POST":
         pass
    

class ProductMixin(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
     
     def get(self, request, *args, **kwargs):
          return self.list(request, *args, **kwargs)
     
     def post(self, request, *args, **kwargs):
          return self.create(request)
     


class Create(mixins.CreateModelMixin, generics.GenericAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
     
     def post(self, request, *args, **kwargs):
          return self.create(request)
     
     
class ProductRetrieveView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProductDestroyView(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)   