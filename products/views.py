from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from .models import Product, CartItem,ShippingAddress
from .forms import ShippingAddressForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from .models import ShippingAddress
from user.models import User


class ProductView(TemplateView):
    template_name = 'base/index.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        data = Product.objects.all()
        context['data']  = data
        return context

class Product_details(TemplateView):
    template_name = 'products/product_details.html'
    model = Product

    def get_context_data(self,id,  **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('id')
        print('id: ', id)
        product = Product.objects.get(pk=id)
        context['product'] =  product
        print('product: ', product)     
        return context

class AddToCart(View):
    """
    return product quantity and product id
    """
    def post(self,request):
        quantity = request.POST.get('quantity')
        product_id = request.POST.get('product_id')
        print('quantity:',quantity)
        print('product_id:',product_id)
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product_id=product_id)
        
        response = {}
        if not created:
            quantity = int(quantity)
            cart_item.quantity = int(quantity)
            cart_item.save()

            response = {'message': 'cart item updated successfully',
                        'quantity': quantity}
        else:
            cart_item.quantity += quantity
            cart_item.save()
            response = {'message': 'product added into cart successfully',
                        'quantity': quantity}
        return JsonResponse(response)

class CartView(View):
    """
    return product item's image in cart
    """
    model = ShippingAddress
    def get(self, request):
        
        user = User.objects.get(email= request.user.email)
        context = {}
        product_item = CartItem.objects.filter(user = user)
        print('product_item: ', product_item)
        context['product_item'] = product_item
        return render(request, 'products/cart.html', context)

"""return shipping address"""
class Add_Address(View):
    def get(self, request):
        form = ShippingAddressForm()
        return render(request, 'products/address.html',{'form':form})

    def post(self, request):
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            user = request.user
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            phone_no = form.cleaned_data.get('phone_no')
            email = form.cleaned_data.get('email')
            country = form.cleaned_data.get('country')
            state = form.cleaned_data.get('state')
            city = form.cleaned_data.get('city')
            address_line1 = form.cleaned_data.get('address_line1')
            address_line2 = form.cleaned_data.get('address_line2')
            zipcode = form.cleaned_data.get('zipcode')

            x = ShippingAddress(user=user, fname=fname,lname=lname,email=email,city=city,phone_no=phone_no, country=country,state=state,address_line1=address_line1,address_line2=address_line2,zipcode=zipcode)
            x. save()
            return redirect('cartview')
        return render(request, 'products/address.html',{'form':form})
    success_url = reverse_lazy('cartview')

class CheckOut(View):
    models = ShippingAddress
    form = ShippingAddress()
    template_name = 'products/checkout.html'

class ContactInfo(TemplateView):
    """
    show contact template
    """
    template_name = 'products/contact.html'
