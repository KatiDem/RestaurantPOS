from django.urls import path, include
from .views import TokenObtainPairView, TokenRefreshView, PasswordChangeView, PasswordResetView, \
    PasswordResetConfirmView, UserViewSet

app_name = 'auth'

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/profile', UserViewSet.as_view(), name='profile'),
    path('auth/reset-password', PasswordResetView.as_view(), name='rest_password_reset'),
    path('auth/reset-password-confirm', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    path('auth/set-password', PasswordChangeView.as_view(), name='rest_password_change'),
]
