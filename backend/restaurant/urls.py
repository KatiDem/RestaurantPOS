from django.urls import path, include
from .views import *

app_name = 'restaurant'

urlpatterns = [
    path('orderitem/create', OrderItemCreateView.as_view()),
    path('orderitem/list', OrderItemListView.as_view()),
    path('orderitem/delete', OrderItemDestroyView.as_view()),
    path('orderitem/update', OrderItemUpdateView.as_view()),
]
