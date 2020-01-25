from django.contrib import admin
from django.urls import path, include

from inventory import views

app_name = 'inventory'

urlpatterns = [
    path('', views.item_list, name='item_list')
]