from django.conf import settings
from django.db import models
from rest_framework.reverse import reverse as api_reverse
from utils.mixins import TimestampMixin


class CookManager(models.Manager):
    def get_queryset(self):
        return super(CookManager, self).get_queryset().select_related('user')


def upload_avatar_image_dir(instance, filename):
    return f'avatars/admin/{filename.lower()}'


class Cook(TimestampMixin):
    objects = CookManager()
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                verbose_name='Повар',
                                on_delete=models.CASCADE,
                                primary_key=True,
                                related_name='cook')
    avatar = models.ImageField('Фотография', upload_to=upload_avatar_image_dir, null=True, blank=True)

    class Meta:
        verbose_name = 'Повар'
        verbose_name_plural = 'Повара'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    # @staticmethod
    # def get_number_of_admins():
    #     return Cook.odjects.count()

    def get_api_url(self, request=None):
        return api_reverse('users:cook-profile-detail', kwargs={'pk': self.user.pk}, request=request)