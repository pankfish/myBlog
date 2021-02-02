from django.db import models



# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=15, null=True)
    message = models.TextField()
