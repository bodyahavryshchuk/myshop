from .serializers import *
from rest_framework import generics
from shop.models import *
from rest_framework import permissions


class CartList(generics.ListAPIView):
    serializer_class = CartListSerializer
    #queryset = Cart.objects.all()

