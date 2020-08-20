from rest_framework import serializers
from shop.models import *


class ProductListSerializer(serializers.ModelSerializer):
    """Список продуктов"""
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'category')


class CommentSerializer(serializers.ModelSerializer):
    """Список комментариев"""

    class Meta:
        model = Comment
        exclude = ('updated',)
        #filter_by = ('active',)


class CommentUpdateSerializer(serializers.ModelSerializer):
    """ Список комментариев для админа"""
    class Meta:
        model = Comment
        fields = '__all__'


class ProductRetrieveSerializer(serializers.ModelSerializer):
    """Детальная информация про продукт"""
    comments = CommentSerializer(many=True)

    class Meta:
        model = Product
        fields = ('category', 'name', 'name', 'image', 'description', 'price', 'available',
                  'created', 'updated', 'comments')


class ProductUpdateRetrieveSerializer(serializers.ModelSerializer):
    """Детальная информация про продукт, изменение, удаление"""

    class Meta:
        model = Product
        fields = ('category', 'name', 'name', 'image', 'description', 'price', 'available',
                  'created', 'updated', 'comments')


class CategorySerializer(serializers.ModelSerializer):
    """Список категорий"""
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')




