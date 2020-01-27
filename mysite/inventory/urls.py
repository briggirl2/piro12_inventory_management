from django.urls import path

from inventory import views

app_name = 'inventory'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('detail/<int:pk>', views.item_detail, name='item_detail'),
    path('create/', views.item_create, name='item_create'),
    path('update/<int:pk>', views.item_update, name='item_update'),
    path('delete/<int:pk>', views.item_delete, name='item_delete'),
    path('plus/<int:pk>', views.item_plus, name='item_plus'),
    path('minus/<int:pk>', views.item_minus, name='item_minus'),

    path('company/', views.company_list, name='company_list'),
    path('company/detail/<int:pk>', views.company_detail, name='company_detail'),
    path('company/create/', views.company_create, name='company_create'),
    path('company/update/<int:pk>', views.company_update, name='company_update'),
    path('company/delete/<int:pk>', views.company_delete, name='company_delete'),
]