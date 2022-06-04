from django.contrib import admin
from .models import Product, CartItem,ShippingAddress

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','category','image','title','brand','discount_price','price','description']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id','user','product']

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['id','fname','lname', 'phone_no','email','address_line1','address_line2','city']
