from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework import permissions
# Create your views here.


class ProductList(ListCreateAPIView):

    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Product.objects

class ProductDetailView(RetrieveUpdateAPIView):

    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    lookup_field = "id"


    def get_queryset(self):
        return Product.objects