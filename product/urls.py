from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetail.as_view()),
    path('create/', views.ProductCreate.as_view()),
    path('list/', views.ProductList.as_view()),
    path('mix/', views.ProductMixin.as_view()),
    path('mix_create/', views.Create.as_view()),
    path('products/<int:pk>/', views.ProductRetrieveView.as_view()),
    path('products/<int:pk>/', views.ProductDestroyView.as_view()),
]