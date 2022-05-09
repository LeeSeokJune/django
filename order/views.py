from django.shortcuts import render
from rest_framework.response import Response
from .models import UserOrder, UserOrderDetail

# Create your views here.

def userorder(request):
    # 주문 했을때
    if request.method == 'POST':
        return Response('주문')
    # 주문 확인
    elif request.method == 'GET':
        
        print('GET')
        return Response('출력')

def nonuserorder(request):
    # 주문 했을때
    if request.method == 'POST':
        return Response('주문')
    # 주문 확인
    elif request.method == 'GET':
        print('GET')
        return Response('출력')