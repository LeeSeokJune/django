from django.db import models
from user.models import User
# Create your models here.
class Product(models.Model):
    p_id =    models.AutoField(primary_key=True)
    p_pet = models.CharField(max_length=100, default='dog')
    p_name =  models.CharField(max_length=100,blank = True)
    p_brand = models.CharField(max_length=100,blank = True)
    p_brief_description =     models.TextField(blank = True)
    p_detail_description =    models.TextField(blank = True)
    p_large_category = models.CharField(max_length=100, blank = True)
    p_medium_category = models.CharField(max_length=100, blank = True)
    p_small_category1 = models.CharField(max_length=100, blank = True)
    p_small_category2 = models.CharField(max_length=100, blank = True)
    p_small_category3 = models.CharField(max_length=100, blank = True)
    p_small_category4 = models.CharField(max_length=100, blank = True)
    p_small_category5 = models.CharField(max_length=100, blank = True)
    p_small_category6 = models.CharField(max_length=100, blank = True)
    p_small_category7 = models.CharField(max_length=100, blank = True)
    p_small_category8 = models.CharField(max_length=100, blank = True)
    p_retail_price = models.IntegerField(blank = True)
    p_wholesale_price = models.IntegerField(blank = True)
    p_product_count = models.IntegerField(blank = True)
    
    def __str__ (self):
        return self.p_name

class Photo(models.Model):
    p_id =    models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', db_column='product_id')
    image =         models.ImageField(upload_to = 'images/',blank=True, null=True)

class Review(models.Model):
    r_id = models.AutoField(primary_key=True)
    p_id = models.ForeignKey(Product, on_delete= models.CASCADE)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    r_content = models.TextField()
    r_date = models.DateField(auto_now_add=True)
    r_help = models.IntegerField(default=0) #도움이 됐다는 표시 숫자
    def __str__(self):
        return self.p_id.name

    def inputReview(request):
        review_info = Review()
        review_info.p_id = Product.objects.get(p_id = int(request.POST['p_id']))
        review_info.u_id = User.objects.get(u_id = int(request.POST['u_id']))
        review_info.r_content = request.POST['r_content']
        review_info.r_help = int(request.POST['r_help'])
        return review_info

class QnA(models.Model):
    q_id = models.AutoField(primary_key = True)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    q_title = models.CharField(max_length=100)
    q_content = models.TextField()
    q_date = models.DateField(auto_now_add = True)
    def inputQnA(request):
        QnA_info = QnA()
        QnA_info.p_id = Product.objects.get(p_id = int(request.POST['p_id']))
        QnA_info.u_id = User.objects.get(u_id = int(request.POST['u_id']))
        QnA_info.q_title = request.POST['q_title']
        QnA_info.q_content = request.POST['q_content']
        
        return QnA_info
