from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import validate_email, RegexValidator
# from rest_framework.reverse import reverse as api_reverse

# from utils.mixins import TimestampMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(
            self, first_name, last_name, email, phone_number,
            is_cook=False, is_waiter=False,
            is_admin=False, is_superuser=False, password=None):
        if not email:
            raise ValueError('Email обязателен!')
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            is_cook=is_cook,
            is_waiter=is_waiter,
            is_admin=is_admin,
            is_superuser=is_superuser,
            phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, phone_number, password):
        user = self.create_user(
            first_name, last_name, email, phone_number, password=password,
            is_cook=True,
            is_waiter=True,
            is_admin=True,
            is_superuser=True
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Телефон должен быть в формате: '+375296788767'")

    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    email = models.EmailField(
        'Email', max_length=255, unique=True, validators=[validate_email])
    phone_number = models.CharField(
        'Телефонный номер',
        validators=[phone_regex],
        max_length=17,
        unique=True)
    is_waiter = models.BooleanField('Официант', default=False)
    is_cook = models.BooleanField('Повар', default=False)
    is_admin = models.BooleanField('Администратор', default=False)
    is_active = models.BooleanField('Активный', default=True)
    is_superuser = models.BooleanField('Суперюзер', default=False)
    is_staff = models.BooleanField('Сотрудник', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    class Meta:
        ordering = ['is_admin']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Все пользователи'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_full_name()

    # def get_api_url(self, request=None):
    #     return api_reverse('users:user-detail', kwargs={'pk': self.pk}, request=request)
