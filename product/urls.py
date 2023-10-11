from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetail.as_view()),
    path('create/', views.ProductCreate.as_view()),
    path('list/', views.ProductList.as_view()),
]