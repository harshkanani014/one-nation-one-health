# Create your models here.
from enum import unique
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.TextField(max_length=100)
    username = models.TextField(default="a")
    mobile = models.BigIntegerField(unique=True)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_pharmacist = models.BooleanField(default=False)
    isVerified = models.BooleanField(blank=False, default=True)
    counter = models.IntegerField(default=0, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'mobile'
    

    def __str__(self):
        return str(self.Mobile)

#class UserManager(A)