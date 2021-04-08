from django.conf import settings
from django.db import models
from .custom_user import CustomUser
# from rest_framework.reverse import reverse as api_reverse


class AdminManager(models.Manager):
    def get_queryset(self):
        return super(AdminManager, self).get_queryset().select_related('user')


def upload_avatar_image_dir(instance, filename):
    return f'avatars/admin/{filename.lower()}'


class Admin(models.Model):
    objects = AdminManager()
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name='admin')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='admin')
    avatar = models.ImageField('Фотография', upload_to=upload_avatar_image_dir, null=True, blank=True)

    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @staticmethod
    def get_number_of_students():
        return Admin.odjects.count()

    # def get_api_url(self, request=None):
    #     return api_reverse('users:student-profile-detail', kwargs={'pk': self.user.pk}, request=request)