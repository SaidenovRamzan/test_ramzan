# # tasks.py
# from threading import Thread
# import time
# from .models import Order

# def process_order_with_delay(order):
#     # Здесь вы можете добавить логику обработки заказа
#     # Например, изменение статуса заказа
#     order.status = 'В работе'
#     order.save()

#     # Задержка на 10 секунд (можно заменить на вашу логику)
#     time.sleep(10)

#     # Изменение статуса заказа после обработки
#     order.status = 'В работе'
#     order.save()

# def process_selected_orders(queryset):
#     threads = []
#     for order in queryset:
#         thread = Thread(target=process_order_with_delay, args=(order,))
#         thread.start()
#         threads.append(thread)

#     # Дождитесь завершения всех потоков
#     for thread in threads:
#         thread.join()
from celery import shared_task
import time

@shared_task
def process_order_task(order_id):
    # Здесь можно добавить логику для обработки заказа, например, изменить его статус
    from .models import Order

    order = Order.objects.get(id=order_id)
    order.status = 'В работе'
    order.save()

    # Имитация задержки в 10 секунд
    time.sleep(10)

    order.status = 'Готово'
    order.save()
