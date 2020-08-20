from django.urls import path

from . import views
app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    #path('produts/', views.ProductList.as_view(), name='product_list'),
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:category_slug>/', views.product_list, name='by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

    path('categories/', views.categories_list, name='categories_list'),
]