from WSS.models import SELLER,CUSTOMER,ADMIN
from WSS.serializers import SELLER_Serializer,CUSTOMER_Serializer,ADMIN_Serializer
from rest_framework import viewsets

class SELLER_ViewSet(viewsets.ModelViewSet):
    queryset = SELLER.objects.all()
    serializer_class = SELLER_Serializer

class CUSTOMER_ViewSet(viewsets.ModelViewSet):
    queryset = CUSTOMER.objects.all()
    serializer_class = CUSTOMER_Serializer

class ADMIN_ViewSet(viewsets.ModelViewSet):
    queryset = ADMIN.objects.all()
    serializer_class = ADMIN_Serializer