# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)

    def __str__(self):
        return self.username
