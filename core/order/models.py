from django.db import models
from django.contrib.auth.models import User
import random

class Order(models.Model):
    order_number = models.CharField(max_length=6, unique=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, default='pending')
    file = models.FileField(upload_to='media/file/')

    def __str__(self):
        return self.order_number
    
    def save(self, *args, **kwargs):
        while True:
            random_number = str(random.randint(100000, 999999))
            if not Order.objects.filter(order_number=random_number).exists():
                self.order_number = random_number
                break
        super(Order, self).save(*args, **kwargs)
