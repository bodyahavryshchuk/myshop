from django.urls import path, include

urlpatterns = [
    path('shop/', include('api.shop_api.urls')),
    path('cart/', include('api.cart_api.urls')),
    path('order/', include('api.order_api.urls')),
]
