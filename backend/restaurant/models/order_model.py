from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta, date


class Order(models.Model):

    # payment = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=True, null=True)  # order of payment
    # table = models.ForeignKey(Seating, on_delete=models.CASCADE)
    time = models.DateTimeField()  # The time at which the order was taken
    # items = models.ManyToManyField(OrderItem)
    cooking_instructions = models.CharField(max_length=500, default='na')  # Preferences, allergies, etc.
    purchase_method = models.CharField(max_length=100, default='na')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    confirmed = models.BooleanField(default=False)  # order has been confirmed
    cancelled = models.BooleanField(default=False)
    ready_delivery = models.BooleanField(default=False)  # order is ready for delivery
    delivered = models.BooleanField(default=False)  # order has been delivered
    delayed = models.BooleanField(default=False)  # order is delayed
    paid = models.BooleanField(default=False)  # order has been paid

