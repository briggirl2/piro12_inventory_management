from django.contrib import admin
from django.urls import path, include

from inventory import views

app_name = 'inventory'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('detail/<int:pk>', views.item_list, name='item_detail'),
    path('company/', views.company_list, name='company_list'),
    path('company/detail/<int:pk>', views.company_detail, name='company_detail'),

]