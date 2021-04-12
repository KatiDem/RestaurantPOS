from django.contrib import admin

from .models.custom_user import CustomUser
from .models.admin import Admin
from .models.cook import Cook
from .models.waiter import Waiter

admin.site.register(CustomUser)
admin.site.register(Admin)
admin.site.register(Cook)
admin.site.register(Waiter)

