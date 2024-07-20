from django.db import models
from datetime import datetime


# Create your models here.


class customer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    address =models.CharField(max_length=100, null=False, blank=False)
    mobile_no = models.CharField(max_length=100, null=False, blank=False)
    balance = models.DecimalField(max_digits=15, decimal_places=2,null=True, blank=True)

    def __str__(self):
        return self.name


class user(models.Model):
    email = models.CharField(max_length=100, null=False, blank=False)
    passowrd =models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    type = models.BooleanField(default=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.email



class Supplier(models.Model):
    supplier_name =models.CharField(max_length=100, null=True, blank=False)
    mobile = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.supplier_name







class category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name




class Brand(models.Model):
    b_name = models.CharField(max_length=100,null=True)
    name = models.ForeignKey(category, on_delete=models.CASCADE,null=True,blank=False)

    status = models.BooleanField(default=True)


    def __str__(self):
        return self.b_name

class product(models.Model):
    pname = models.CharField(max_length=100, null=False, blank=False)
    model = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(max_length=100, null=False, blank=False)
    quantity = models.IntegerField(default=0, blank=True, null=True, unique=True, )
    unit = models.CharField(max_length=100, null=False, blank=False)
    base_price = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.DecimalField(max_digits=15, decimal_places=2)
    min_ord = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=False)
    supplier = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(category, on_delete=models.CASCADE, null=True, blank=False)
    b_name = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=False)
    supplier_name = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)



    def __str__(self):
        return self.pname

class purchase(models.Model):
    supplier_id = models.CharField(max_length=100, null=False, blank=False)
    product_id = models.CharField(max_length=100, null=False, blank=False)
    quantity = models.CharField(max_length=100, null=False, blank=False)
    purchese_date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quantity



class order(models.Model):
    product_id = models.CharField(max_length=100, null=False, blank=False)
    total_shipped = models.IntegerField(default=0,  blank=True,null=True,  unique=True,)
    customer_id = models.IntegerField(default=0,  blank=True,null=True,  unique=True,)
    order_date =  models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product_id
