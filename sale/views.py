from django.shortcuts import render
# Create your views here.
from rest_framework.generics import ListCreateAPIView
from .models import Sale
from products.models import Product
from .serializers import SaleSerializer
from rest_framework import permissions


class SaleList(ListCreateAPIView):

    serializer_class = SaleSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)


    def get_queryset(self):
        My_sale= Sale.objects.filter(owner=self.request.user)
        
        for i in My_sale:
            q = i.quantity
            ii = i.product
            cost = int(q)*int(ii.price)
            i.price = cost

        return My_sale
        
