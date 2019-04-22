from django.contrib.auth.models import AbstractUser
from django.db import models





class User(AbstractUser):
    # add additional fields in here
    phone_number = models.IntegerField(verbose_name='Phone number')
    
    def __str__(self):
        return self.email