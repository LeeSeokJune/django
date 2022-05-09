from django.db import models
from user.models import User
from product.models import Product
# Create your models here.



class ShoppingCart(models.Model):
    s_id = models.AutoField(primary_key=True)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    s_count = models.IntegerField(default=1)

    def inputShoppingCart(request):
        cart_info = ShoppingCart()
        cart_info.u_id = User.objects.get(u_id = int(request.POST['u_id']))
        cart_info.p_id = Product.objects.get(p_id = int(request.POST['p_id']))
        return cart_info
