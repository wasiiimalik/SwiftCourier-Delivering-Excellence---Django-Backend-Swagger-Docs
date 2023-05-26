from rest_framework import serializers
from .models import Order, Customer, Driver, DeliveryStatus

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class DeliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryStatus
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    driver = DriverSerializer()
    delivery_status = DeliveryStatusSerializer()

    class Meta:
        model = Order
        fields = '__all__'
