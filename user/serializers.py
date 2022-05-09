from dataclasses import field
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('u_id','u_strid', 'u_name','u_pw')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('u_strid','u_pw','u_name')
