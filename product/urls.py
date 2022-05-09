from django.urls import URLPattern, path, include
from .views import item_list,item_detail, review
urlpatterns = [
    path('items', item_list),
    path('items/<int:p_id>', item_detail),
    path('review/<int:p_id>', review),
]