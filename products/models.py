from unicodedata import category
from django.db import models
from user.models import User

category_choices = (
    ('clothes','Clothes',),
    ('shoes','Shoes'),
    ('electric','Electric')
)

class Product(models.Model):
    category = models.CharField(max_length=20,choices = category_choices,null=True, blank=True)
    image = models.ImageField(upload_to='products')
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    discount_price = models.IntegerField(null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def get_quantity(self):
        data = self.cartitem_set.all().first()
        return data.quantity
        


class CartItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_total(self):
        return self.quantity*self.product.discount_price

    def __str__(self):
        return str(self.product)

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    email = models.EmailField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=200)
    address_line2= models.CharField(max_length=200)
    zipcode = models.IntegerField()

    def __str__(self):
        return str(self.user)
