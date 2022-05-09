from django.db import models
from django.contrib.postgres.fields import ArrayField
# from product.models import Product

# Create your models here.
class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_strid = models.CharField(max_length=20)
    u_pw = models.CharField(max_length = 20)
    u_name = models.CharField(max_length = 20, default='')
    u_phone = models.CharField(max_length=20, blank = True)
    u_post = models.CharField(max_length=20, blank = True)
    u_date = models.DateField(auto_now_add= True) #가입일
    # u_birth = models.DateField(blank=True)
    u_drop = models.BooleanField(default=False) #회원 탈퇴 여부
    #u_shopping_cart = ArrayField(base_field=models.IntegerField(blank=True), blank= True)

    def __str__ (self):
        return self.u_name
    
    def inputUser(request):
        user_info = User()
        user_info.u_strid = request.POST['u_strid']
        user_info.u_pw = request.POST['u_pw']
        user_info.u_name = request.POST['u_name']
        #user_info.u_phone = request.POST['u_phone']
        #user_info.u_post = request.POST['u_post']
        #user_info.birth = request.POST['u_id']
        #user_info.u_drop = request.POST['u_']
        #user_info.u_shopping_cart = request.POST['u_id']
        return user_info

    # def has_shoppingcart_item(self, item):
    #     return item in self.u_shopping_cart
    
    # def add_shoppingcart_item(self, item):
    #     if self.has_shoppingcart_item(item):
    #         return
    #     self.u_shopping_cart.append(item)
    #     self.save(update_fields=['shoppingcart'])

    # def remove_shoppingcart_item(self, item):
    #     if not self.has_shoppingcart_item:
    #         return
    #     self.u_shopping_cart.remove(item)
    #     self.save(update_fields=['shoppingcart'])
    #     return self.u_shopping_cart
