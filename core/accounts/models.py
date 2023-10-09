from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField()
    age = models.IntegerField(null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def save (self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        
        return super().save(force_insert, force_update, using, update_fields)
