from django.contrib import admin
from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админмодель заказа"""
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]