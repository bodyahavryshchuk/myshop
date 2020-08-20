from .serializers import *
from rest_framework import generics
from orders.models import *
from rest_framework import permissions


class OrderList(generics.ListAPIView):
    """Список заказов"""
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


class OrderCreate(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    queryset = OrderItem.objects.all()


