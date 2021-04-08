from django.db import models


class TimestampMixin(models.Model):
    created_at = models.DateTimeField('Created by', auto_now_add=True)
    updated_at = models.DateTimeField('Last update', auto_now=True)

    class Meta:
        abstract = True