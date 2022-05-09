from django.urls import URLPattern, path, include
from .views import userorder
urlpatterns = [
    path('userorder', userorder),
]