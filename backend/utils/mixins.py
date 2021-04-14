from django.db import models


class TimestampMixin(models.Model):
    created_at = models.DateTimeField('Created by', auto_now_add=True)
    updated_at = models.DateTimeField('Last update', auto_now=True)

    class Meta:
        abstract = True


class CreateListModelMixin(object):

    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)