from django.urls import path
from . import views

urlpatterns = [
    path('cart_list/', views.CartList.as_view(), name='cart_api'),

]
