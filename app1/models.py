from django.db import models

class StockerRegister(models.Model):
    idn = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_Number = models.IntegerField(unique=True)
    Password = models.CharField(max_length=50)

class Dispatcher_Register(models.Model):
    idno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Contact_Number = models.IntegerField(unique=True)
    password = models.CharField(max_length=50)

class Product_Details(models.Model):
    Product_no = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=150)
    Price = models.IntegerField()
    Quality = models.CharField(max_length=150)
    Quantity = models.IntegerField(default=0)
    Add_Date = models.DateField(auto_now_add=True)
