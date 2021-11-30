from django.db import models
from django.utils import timezone


class Pet(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(default=timezone.now)
    is_birth_approximate = models.BooleanField()
    
    def __str__(self) -> str:
        return self.name
    

class User(models.Model):
    username = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=False)
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=50)