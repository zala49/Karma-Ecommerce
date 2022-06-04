from django.urls import path
from .views import CartView, ProductView, Product_details, AddToCart, Add_Address, CheckOut,ContactInfo


# User's Urls
urlpatterns = [
    path('', ProductView.as_view(), name="product_show"),
    path('<int:id>/product_details/', Product_details.as_view(), name="product_details"),
    path('add_to_cart/', AddToCart.as_view(), name="add_to_cart_url"),
    path('product_cart/', CartView.as_view(), name="cartview"),
    path('address/', Add_Address.as_view(), name="address"),
    path('checkout/', CheckOut.as_view(), name="checkout"),
    path('contact/', ContactInfo.as_view(), name="contact"),
]
