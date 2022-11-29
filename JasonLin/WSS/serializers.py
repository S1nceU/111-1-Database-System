from rest_framework import serializers
from WSS.models import SELLER,CUSTOMER,ADMIN


class SELLER_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SELLER
        fields = '__all__'
class CUSTOMER_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CUSTOMER
        fields = '__all__'        
class ADMIN_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ADMIN
        fields = '__all__'