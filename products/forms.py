from django.forms import ModelForm
from django import forms
from .models import ShippingAddress
# from .models import Product


# class CreateProductForm(ModelForm):
#     class Meta:
#         model=Product
#         fields='__all__'

class ShippingAddressForm(forms.ModelForm):

    fname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    lname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_no = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'class':'form-control'}))
    country = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    state = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    address_line1 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    address_line2 = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    zipcode = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))


    class Meta:
        model = ShippingAddress
        fields=('fname','lname','phone_no','email','country','state','city','address_line1','address_line2','zipcode')  