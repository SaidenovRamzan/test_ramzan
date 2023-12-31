from django.contrib import admin
from .models import Order, FileImageForOrder


class OrderAdmin(admin.ModelAdmin):
    exclude = ['order_number']
    def process_orders(self, request, queryset):
        from celery import shared_task
        from order.tasks import process_order_task 
        
        for order in queryset:
            process_order_task.delay(order.id)
            ...
        self.message_user(request, f'Выбранные заказы переданы в обработку.')

    process_orders.short_description = 'Передать заказы в обработку'
    actions = ['process_orders']


admin.site.register(Order, OrderAdmin)
admin.site.register(FileImageForOrder)


