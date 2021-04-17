from django.urls import path, include
from .views import MenuDeleteView, MenuListView, MenuUpdateView, MenuCreateView

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
]
