from django.db import models
from django.contrib.auth.models import User
import random


class Order(models.Model):
    Choices = [
    ('В ожидании', 'В ожидании'),
    ('В работе', 'В работе'),
    ('Готово', 'Готово'),
    ]
    
    order_number = models.CharField(max_length=6, unique=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(choices=Choices, max_length=20, default='В ожидании')
    
    def __str__(self):
        return self.order_number
    
    def save(self, *args, **kwargs):
        while True:
            random_number = str(random.randint(100000, 999999))
            if not Order.objects.filter(order_number=random_number).exists():
                self.order_number = random_number
                break
        super(Order, self).save(*args, **kwargs)


class FileImageForOrder(models.Model):
    order_file = models.FileField(upload_to='media/file/')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="files")
    
# class OrderFileModel(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     file = models.ForeignKey(FileImageForOrder, on_delete=models.CASCADE)
    
