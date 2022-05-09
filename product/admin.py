from django.contrib import admin
from .models import Product, Photo,Review, QnA
# Register your models here.

class PhotoInline(admin.TabularInline):
    model = Photo

class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]
    list_display = ('p_id', 'p_name', 'p_brand',) #admin에서 요소들을 보여줄수있음
    list_editable = ('p_brand', 'p_name',)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
admin.site.register(QnA)