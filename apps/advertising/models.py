from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from users.models import User


# Create your models here.

class AdvertCategory(models.Model):
    name = models.CharField(max_length=200)


class Advertising(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(AdvertCategory, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    contacts = models.CharField(max_length=200)


class ReviewRating(models.Model):
    advertising = models.ForeignKey(Advertising, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, related_name='reviews')
    review = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )


class Booking(models.Model):
    time_start = models.DateField()
    time_finish = models.DateField()
    advertising = models.ForeignKey(Advertising, on_delete=models.CASCADE)
