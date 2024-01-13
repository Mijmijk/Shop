from django.contrib import admin
from .models import Product, Order
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','image','desc','price','discount','price','rating','stock','is_available')
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('product','delivery_address','created_at')
	list_editable = ('delivery_address',)