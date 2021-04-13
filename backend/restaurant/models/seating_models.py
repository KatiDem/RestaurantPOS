from django.db import models


class Seating(models.Model):
    name_table = models.CharField('Table name', max_length=30, unique=True)
    status = models.BooleanField('Status', default=False, help_text='If the table is busy-True, free-False')
    # waiter = models.ForeignKey('Waiter', on_delete=models.CASCADE, verbose_name='Waiter')

    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'
        ordering = ['status']

    def __str__(self):
        return self.name_table
