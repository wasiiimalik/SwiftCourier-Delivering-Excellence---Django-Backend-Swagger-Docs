from django.db import models

# Create your models here.
from django.db import models

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', on_delete=models.SET_NULL, null=True)
    delivery_status = models.ForeignKey('DeliveryStatus', on_delete=models.CASCADE)
    # Add other fields as per your requirements

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Add other fields as per your requirements

class Driver(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as per your requirements

class DeliveryStatus(models.Model):
    status = models.CharField(max_length=100)
    # Add other fields as per your requirements
