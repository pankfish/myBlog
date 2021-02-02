from django.db import models
from django.urls import reverse

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=13)
    description = models.TextField(null=True)

