from django.urls import path, include
from .views import *

app_name = 'users'

urlpatterns = [
    path('user/create/', CustomUserCreateView.as_view()),
    path('user/list/', CustomUserListView.as_view()),
    path('user/<str:pk>', CustomUserRetrievView.as_view()),
    path('user/del/<str:pk>', CustomUserDestroyView.as_view()),
    path('admin/create/', AdminCreateView.as_view()),
    path('admin/list/', AdminListView.as_view()),
    path('admin/<str:pk>', AdminRetrievView.as_view()),
    path('admin/del/<str:pk>', AdminDestroyView.as_view())
]