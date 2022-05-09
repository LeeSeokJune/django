from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import User
from .serializers import UserSerializer,UserSimpleSerializer
# Create your views here.


@api_view(['GET','POST'])
def user(request,pk):
    
    #모든 유저의 정보 -> 관리자용
    
    if request.method=="GET":
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    # 로그인, 회원가입
    elif request.method=='POST':
        #로그인하면 데이터를 넘겨줘야 할거같음
        if pk==0:
            print(request.POST)
            try :
                uInfo = User.objects.get(u_strid = request.POST['u_strid'])
                serializer = UserSimpleSerializer(uInfo)
            except : 
                print('fail')
                return Response('fail')
            else :
                print('done')
                return Response(serializer.data) #serializer로 바꿔야할듯
            
        #회원가입
        elif pk==1:
            user_info = User.inputUser(request)
            
            try:
                uInfo = User.objects.get(u_id = request.POST['u_id'])
            except:
                print('done')
                user_info.save()
                return Response('done')
            else:
                print('fail')
                return Response('fail')
            
            # serializer = UserSerializer(queryset)
