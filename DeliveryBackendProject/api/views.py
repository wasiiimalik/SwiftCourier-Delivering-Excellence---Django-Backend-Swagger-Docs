from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from .models import Order, Customer, Driver, DeliveryStatus
from .serializers import OrderSerializer, CustomerSerializer, DriverSerializer, DeliveryStatusSerializer

class CustomAPIException(APIException):
    def __init__(self, detail):
        self.detail = detail

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        try:
            # Your create logic here
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        except Exception as e:
            raise CustomAPIException(detail=str(e))

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def update(self, request, *args, **kwargs):
        try:
            # Your update logic here
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except Exception as e:
            raise CustomAPIException(detail=str(e))

class DeliveryStatusViewSet(viewsets.ModelViewSet):
    queryset = DeliveryStatus.objects.all()
    serializer_class = DeliveryStatusSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            # Your destroy logic here
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=204)
        except Exception as e:
            raise CustomAPIException(detail=str(e))
