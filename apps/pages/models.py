from django.db import models


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=9, default='94', blank=False, unique=True, )
    message = models.TextField()

    def __str__(self):
        return self.name
