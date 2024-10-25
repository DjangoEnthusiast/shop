from django.db import models
from django.utils import timezone
from django.core import validators

# Create your models here.

class Member(models.Model):
    name=models.CharField(max_length=255)
    shop_name=models.CharField(max_length=255)
    image=models.FileField(upload_to='images')
    email_id=models.EmailField(unique=True)
    username=models.CharField(max_length=255, unique=True)
    password=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    usertype=models.CharField(max_length=50,null=True)

class Product(models.Model):
    productimage=models.FileField(upload_to='images')
    productname=models.CharField(max_length=255)
    productquantity=models.CharField(max_length=255)
    productdescription=models.CharField(max_length=255)
    inthebox=models.CharField(max_length=500,null=True)
    displaytype=models.CharField(max_length=255,null=True)
    batterycapacity=models.CharField(max_length=255,null=True)
    processorbrand=models.CharField(max_length=255,null=True)
    internalstorage=models.CharField(max_length=255,null=True)
    ram=models.CharField(max_length=255,null=True)
    primarycamera=models.CharField(max_length=255,null=True)
    operatingsystem=models.CharField(max_length=255,null=True)
    memorycardslottype=models.CharField(max_length=255,null=True)
    supportednetworks=models.CharField(max_length=255,null=True)
    warrantysummary=models.CharField(max_length=255,null=True)
    productprice=models.CharField(max_length=255)
    category=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=2000,null=True)

class Category(models.Model):
    categoryname=models.CharField(max_length=50,null=True)

class Cart(models.Model):
    products = models.ManyToManyField('Product')

class deliverydetails(models.Model):
    customer_name=models.CharField(max_length=255)
    customer_address=models.CharField(max_length=500)
    customer_city=models.CharField(max_length=50,null=True)
    customer_state=models.CharField(max_length=50,null=True)
    customer_contact=models.CharField(max_length=50)
    customer_pincode=models.CharField(max_length=6)
    customer_email=models.CharField(max_length=225)

class savedcard(models.Model):
    card_holder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16, validators=[validators.MaxLengthValidator(16)])
    expiry_date = models.CharField(max_length=5, validators=[validators.MaxLengthValidator(5)])
    cvv = models.CharField(max_length=3, validators=[validators.MaxLengthValidator(3)])

class order(models.Model):
    customer_name=models.CharField(max_length=255)
    customer_address=models.CharField(max_length=500)
    customer_city=models.CharField(max_length=50,null=True)
    customer_state=models.CharField(max_length=50,null=True)
    customer_contact=models.CharField(max_length=50)
    customer_pincode=models.CharField(max_length=6)
    customer_email=models.CharField(max_length=225)
    productname=models.CharField(max_length=255)
    productquantity=models.CharField(max_length=255)
    productprice=models.CharField(max_length=255)
    oid = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
