from .serializers import *
from rest_framework import generics
from shop.models import *
from rest_framework import permissions


class ProductsList(generics.ListAPIView):
    """Список продуктов"""
    serializer_class = ProductListSerializer
    queryset = Product.objects.filter(available=True)


class ProductRetrieve(generics.RetrieveAPIView):
    """Детальная информация про продукт"""
    serializer_class = ProductRetrieveSerializer
    queryset = Product.objects.all()


class ProductCreate(generics.CreateAPIView):
    """Создание продукта"""
    serializer_class = ProductUpdateRetrieveSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Детальная информация про продукт, изменение, удаление"""
    serializer_class = ProductUpdateRetrieveSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class CategoriesList(generics.ListAPIView):
    """Список категорий"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryCreate(generics.CreateAPIView):
    """Создание категории"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Детальная информация про категорию, изменение, удаление"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class CommentCreate(generics.CreateAPIView):
    """Создание комментария"""
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentUpdateSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
