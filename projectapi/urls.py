from django.urls import path
from . import views

urlpatterns = [
    path('getdata/', views.getData),
    path('getdata/<str:title>/', views.getByTitle)
]