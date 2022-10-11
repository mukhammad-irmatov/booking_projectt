from django.db import models
from phone_field import PhoneField


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone = PhoneField(max_length=9, default='94', blank=False, unique=True, help_text='Contact phone number')
    message = models.TextField()

    def __str__(self):
        return self.name
