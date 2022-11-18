from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, phone, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not phone:
            raise ValueError('The given email must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


phone_regex = RegexValidator(
    regex=r'^+998[0-9]{9}$',
    message="Phone number must be entered in the format: '+998 [XX] [XXX XX XX]'. Up to 13 digits allowed."
)


class User(AbstractUser):

    class User_roles(models.TextChoices):
        ordinary_user = "ordinary", "Ordinary"
        client_user = "client", "Client"

    user_role = models.CharField(max_length=10,
                                 choices=User_roles.choices,
                                 default=User_roles.ordinary_user
                                 )
    phone = models.CharField(max_length=13, validators=[phone_regex], unique=True)
    is_verified = models.BooleanField(default=False)
    username = None
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
