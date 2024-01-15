from django.db import models
from django.contrib.auth.models import AbstractUser


class SchoolManagerModel(AbstractUser):
    ADMIN = 'admin'
    PARENT = 'parent'
    CHOICES = [
        (ADMIN, 'admin'),
        (PARENT,'parent')
    ]
    role = models.CharField(max_length=50,choices=CHOICES)
    tel = models.CharField(max_length=50)