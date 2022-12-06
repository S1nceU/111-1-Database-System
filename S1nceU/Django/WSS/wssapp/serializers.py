from rest_framework import serializers
from .models import Seller, Customer
class SellerSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Seller
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Customer
        fields = '__all__'
