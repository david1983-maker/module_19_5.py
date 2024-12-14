from django.db import models
from decimal import Decimal


# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=10)
    balance = models.DecimalField(max_digits=100, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=10)
    cost = models.DecimalField(max_digits=100, decimal_places=2)
    size = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='gamers')

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
