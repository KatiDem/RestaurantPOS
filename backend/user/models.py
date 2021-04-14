from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

class User(AbstractUser):
    class Meta:
        db_table = "user"

    ROLES = (
        ('Admin', 'Admin'),
        ('Waiter', 'Waiter'),
        ('Cook', 'Cook'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField("Email", unique=True)
    role = models.CharField(max_length=50, choices=ROLES)
    is_superuser = models.BooleanField(default=False)
    is_waiter = models.BooleanField(default=False)
    is_cook = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.role == 'Admin':
            self.is_superuser = True
        elif self.role == 'Waiter':
            self.is_waiter = True
        elif self.role == 'Cook':
            self.is_cook = True

        super(User, self).save(*args, **kwargs)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def create_password_send_email(self):
        subject = loader.render_to_string('authentication/confirmation-email.txt')
        subject = ''.join(subject.splitlines())

        body = loader.render_to_string('authentication/confirmation-email.html', {
            'uid': urlsafe_base64_encode(force_bytes(self.pk)),
            'token': default_token_generator.make_token(self),
            'user': self,
        })

        self.email_user(subject, body)
