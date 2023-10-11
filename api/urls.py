from django.urls import path
from . import views

urlpatterns = [
    path('',views.api_home),
    path('post/',views.api_home_post),
]