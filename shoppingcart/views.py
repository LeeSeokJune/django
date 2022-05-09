from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import ShoppingCart
from .models import User
from .serializers import ShoppingCartSerializer
# Create your views here.

@api_view(['GET','POST'])
def shoppingcart(request):
    #유저 id(pk)를 통해 유저 불러오고 거기에 shoppingcart에 json 형태로 저장
    if request.method == 'POST': #여기는 쇼핑카트에 저장
        print(request.POST)
        # cart_info = ShoppingCart.inputShoppingCart(request)
        # print(request.POST)
        data = request.POST
        try :
            queryset = ShoppingCart.objects.get(u_id = int(data['u_id']), p_id = int(data['p_id']))
        except:
            cart_info = ShoppingCart.inputShoppingCart(request)
            cart_info.save()
        else : 
            queryset.s_count+=1
            queryset.save()
        return Response('done')
@api_view(['GET','POST'])
def shoppingcart_detail(request):
    #유저의 모든 장바구니 데이터 겟
    data = request.POST
    print(data)
    try : 
        #queryset =  ShoppingCart.objects.filter(u_id = User.objects.filter(u_id = int(data['u_id'])) )
        queryset = ShoppingCart.objects.filter(u_id = int(data['u_id']))
    except : 
        return Response('empty')
    else :
        serializer = ShoppingCartSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)

    