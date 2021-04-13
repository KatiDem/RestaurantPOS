from django.urls import path, include
from .views import *

app_name = 'restaurant'

urlpatterns = [path('table/', TableListView.as_view()),
               path('table/free/', TableFreeListView.as_view()),
               path('table/create/', TableCreateView.as_view()),
               path('table/delete/<int:pk>/', TableDeleteView.as_view()),
               path('table/update/<int:pk>/', TableStatusPatchView.as_view()),
]






