from rest_framework import serializers
from shop.models import *
from orders.models import *


class OrderListSerializer(serializers.ModelSerializer):
    """Список продуктов"""
    class Meta:
        model = Order
        exclude = ['paid']


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        #fields = '__all__'
        exclude = ['price', 'order']


class OrderCreateSerializer(serializers.ModelSerializer):
    #order_item = OrderItemSerializer(slug_field='name')

    class Meta:
        model = OrderItem
        # fields = ('first_name', 'last_name', 'email', 'address', 'postal_code',
        #           'city')
        fields = ('product', 'order')
