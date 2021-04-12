from django.urls import path, include
from .views import *

app_name = 'restaurant'

urlpatterns = [
    path('order/create/',OrderCreateView.as_view()),
    path('order/list/', OrderListView.as_view()),
    path('order/del/<str:pk>', OrderDestroyView.as_view())
]
