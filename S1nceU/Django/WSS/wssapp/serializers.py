from rest_framework import serializers
from .models import SELLER

class SELLERSerializer(serializers.ModelSerializer):   
    class Meta:
        model = SELLER
        fields = '__all__'