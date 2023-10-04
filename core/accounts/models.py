from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
