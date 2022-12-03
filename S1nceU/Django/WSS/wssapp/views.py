from django.shortcuts import get_object_or_404
from .models import Seller, Customer
from .serializers import SellerSerializer, CustomerSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action


# Create your views here.
class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    @action(detail=True,methods=['get'])
    def getSeller(self, request, pk = None):
        seller = get_object_or_404(Seller, pk=pk)
        result = {
            'user_id_s' : seller.user_id_s,
            'username' : seller.username,
            'account' : seller.account,
            'password' : seller.password,
            'email' : seller.email,
            'address' : seller.address,
            'phone' : seller.phone,
            'id_number' : seller.id_number,
            # 'user_status' :  seller.user_status 
        }   
        return Response(result, status=status.HTTP_200_OK)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

