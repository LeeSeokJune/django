from django.urls import URLPattern, path, include
from .views import shoppingcart, shoppingcart_detail
urlpatterns = [
    path('shoppingcart',shoppingcart),
    path('shoppingcartdetail', shoppingcart_detail),
]