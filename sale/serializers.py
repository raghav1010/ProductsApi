from rest_framework.serializers import ModelSerializer
from .models import Sale
from rest_framework import serializers

class SaleSerializer(ModelSerializer):
    price = serializers.CharField(required=False)
    class Meta:
        model = Sale
        fields=['id','product','price','quantity']