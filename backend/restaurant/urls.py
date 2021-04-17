from django.urls import path, include
from .views import *

app_name = 'restaurant'

urlpatterns = [
    path('orderitem/create', OrderItemCreateView.as_view()),
    path('orderitem/list', OrderItemListView.as_view()),
    path('orderitem/delete', OrderItemDestroyView.as_view()),
    path('orderitem/update', OrderItemUpdateView.as_view()),
    path('menu/create/', MenuCreateView.as_view()),
    path('menu/update/<int:pk>/', MenuUpdateView.as_view()),
    path('menu/list/', MenuListView.as_view()),
    path('menu/delete/<int:pk>', MenuDeleteView.as_view()),
    path('order/list/', OrderListView.as_view()),
    path('order/create/', OrderCreateView.as_view()),
    path('order/delete/<str:number>/', OrderDestroyView.as_view()),
    path('order/update/<str:number>/', OrderView.as_view()),

]