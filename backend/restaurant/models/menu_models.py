from django.db import models


class Menu(models.Model):
    table = models.ManyToManyField(Seating, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1000)
    category = models.CharField(max_length=100)
    calories = models.IntegerField(default=0, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    vegan = models.BooleanField(default=False)
    meat = models.BooleanField(default=False)
    comment = models.CharField(max_length=300)