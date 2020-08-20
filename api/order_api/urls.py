from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.OrderList.as_view(), name='orders_list_api'),
    path('create/', views.OrderCreate.as_view(), name='orders_create_api'),

]
