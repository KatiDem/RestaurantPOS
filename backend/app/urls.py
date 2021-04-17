from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


admin.site.site_header = "Restaurant POS Admin panel"
admin.site.site_title = "Restaurant POS"
admin.site.index_title = "Welcome to the control panel Restaurant POS"


urlpatterns = [
    path('main/admin/', admin.site.urls, name='admin'),
    path('main/api/v1/api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('main/api/v1/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('main/api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('main/api/v2/', include('user.urls')),
    path('main/api/v3/', include('restaurant.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
