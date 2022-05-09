from rest_framework import serializers
from .models import UserOrder,UserOrderDetail

class UserOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrder
        fields = '__all__'

class UserOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrderDetail
        fields = '__all__'

