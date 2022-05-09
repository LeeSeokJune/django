from django.urls import URLPattern, path, include
from .views import user
urlpatterns = [
    path('user/<int:pk>',user),

]