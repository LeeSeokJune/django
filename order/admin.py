from django.contrib import admin
from .models import UserOrder,UserOrderDetail
# Register your models here.

class UserOrderDetailInline(admin.TabularInline):
    model = UserOrderDetail

class UserOrderAdmin(admin.ModelAdmin):
    inlines = [UserOrderDetailInline, ]


admin.site.register(UserOrder, UserOrderAdmin)