from rest_framework import serializers
from .models import Product, Photo, Review, QnA

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['image','product_id'] # 여기에 product_id 가 굳이 필요하려나 순서는 필요할지도...


class ProductSerializer(serializers.ModelSerializer):
    images = PhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        #fields = ('id','name','brand','brief_description','detail_description')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
class QnASerializer(serializers.ModelSerializer):
    class Meta:
        model = QnA
        fields = '__all__'