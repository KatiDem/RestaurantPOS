from django.contrib import admin
from .models import Seating




@admin.register(Seating)
class SeatingAdmin(admin.ModelAdmin):
    list_display = ('name_table', 'status')
    list_editable = ('status',)
