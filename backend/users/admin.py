from django.contrib import admin

from .models.custom_user import CustomUser
from .models.admin import Admin

admin.site.register(CustomUser)
admin.site.register(Admin)

