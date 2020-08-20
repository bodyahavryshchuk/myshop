from rest_framework import serializers
from cart.cart import *
from shop.models import *


class CartListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'


