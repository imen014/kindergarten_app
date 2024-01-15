from django.db import models


class Kids_school(models.Model):
    school_name = models.CharField(max_length=255)
    school_location = models.CharField(max_length=255)
    school_owner = models.CharField(max_length=255)
    manager_email = models.CharField(max_length=255)
    manager_tel = models.CharField(max_length=255)

