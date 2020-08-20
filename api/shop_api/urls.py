from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductsList.as_view(), name='product_list_api'),
    path('product/<int:pk>/', views.ProductRetrieve.as_view(), name='product_detail_api'),
    path('product/create/', views.ProductCreate.as_view(), name='product_create_api'),
    path('product/<int:pk>/update', views.ProductRetrieveUpdateDestroy.as_view(), name='product_update_api'),

    path('categories/', views.CategoriesList.as_view(), name='categories_list_api'),
    path('category/create/', views.CategoryCreate.as_view(), name='categories_create_api'),
    path('category/<int:pk>/', views.CategoryRetrieveUpdateDestroy.as_view(), name='category_detail_api'),

    path('comment/create/', views.CommentCreate.as_view(), name='comment_create'),
    path('product/<int:pk>/comment/update', views.CommentUpdate.as_view(), name='comment_update'),
]
