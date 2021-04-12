from django.urls import path, include

from rest_framework import routers

from users.views import AdminProfileViewSet, WaiterProfileViewSet, CookProfileViewSet


app_name = 'users'


router = routers.DefaultRouter()
router.register('profile/admin', AdminProfileViewSet, 'admin-profile')
router.register('profile/waiter', WaiterProfileViewSet, 'waiter-profile')
router.register('profile/cook', CookProfileViewSet, 'cook-profile')


urlpatterns = [
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]