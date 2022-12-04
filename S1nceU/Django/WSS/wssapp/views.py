from django.shortcuts import get_object_or_404
from .models import Seller, Customer
from .serializers import SellerSerializer, CustomerSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

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
    
    # @api_view(['POST'])
    # def PostCustomer(request):
    #     if request.username in Customer.objects.all() :
    #         account = get_object_or_404(Customer, Customer.object.filter(username = request.account))
    #         print(request)

class LoginViewSet(APIView):
    # def get_queryset(self):
    #     user = self.request.user
    # def get_serializer_class(self):
    #     return super().get_serializer_class()
    
    renderer_classes = [JSONRenderer]

    @action(detail=True,methods=['POST'])
    def get_object(self, request, format=None):
        user = self.get_object()
        print(user)

        return Response({"GG":True})

    # if request.method == 'POST':
    #     try:
    #         account = get_object_or_404(Customer, Customer.object.filter(username = request.account))
    #         if request.password == account.password:
    #             return Response(status=status.HTTP_200_OK)
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
