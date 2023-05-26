from django.contrib import admin

# Register your models here.
from .models import Order, Customer, Driver, DeliveryStatus
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass

@admin.register(DeliveryStatus)
class DeliveryStatusAdmin(admin.ModelAdmin):
    pass
