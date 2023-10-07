# admin.py
from django.contrib import admin
from .models import Order, FileImageForOrder
from .tasks import process_selected_orders

class OrderAdmin(admin.ModelAdmin):
    exclude = ['order_number']
    
    actions = ['process_orders_action']

    def process_orders_action(self, request, queryset):
        process_selected_orders(queryset)
    
    process_orders_action.short_description = "Обработать выбранные заказы"
admin.site.register(Order, OrderAdmin)
admin.site.register(FileImageForOrder)
# admin.site.register(OrderFileModel)


