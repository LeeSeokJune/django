from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Photo, Review, QnA
from .serializers import ProductSerializer, ReviewSerializer
import json
# Create your views here.


@api_view(['GET','POST'])
def item_list(request):
    if request.method == 'GET':
        queryset = Product.objects.all()
        print(queryset)
        serializer = ProductSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
    elif request.method =='POST':
        #프론트에서 데이터가 들어오면 그거대로 필터링
        #문법 체크해서 다시 확인
        print(request.POST)
        return Response(request.POST.get("a"))

@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def item_detail(request, p_id):
    queryset = Product.objects.get(id=p_id)
    #개별조회
    if request.method =='GET':  
        serializer = ProductSerializer(queryset)
        return Response(serializer.data)
    #데이터 수정
    #문법이 이게 맞는지 확인해봐야함
    elif request.method =='PUT': 
        queryset = request.PUT
        queryset.save()
    #데이터 삭제
    elif request.method =='DELETE':
        queryset.delete()

@api_view(['GET', 'PUT', 'DELETE','POST'])
def review(request,p_id):
    #p_id = product_id
    #리뷰 생성
    if request.method == 'POST':
        print(request.POST)
        review_info = Review.inputReview(request)
        review_info.save()
        return Response('done')
    # 제품 리뷰 불러오기
    elif request.method == 'GET':
        queryset = Review.objects.filter(p_id = Product.objects.get(p_id = int(p_id)))
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

def qna(request, p_id):
    #p_id 는 
    # qna 생성
    if request.method == 'POST':
        request.POST
        return Response()
    # qna 불러오기
    elif request.method == 'GET':
        queryset = QnA.objects.filter(p_id = p_id)
        return Response()