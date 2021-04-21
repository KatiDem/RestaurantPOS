from django.contrib import admin
from .models import Table, MenuItem, OrderItem, Order

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_available')
    list_editable = ('is_available',)

@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')

@admin.register(OrderItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'quantity', 'total_price')

@admin.register(Order)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'table', 'date_of_creation')

