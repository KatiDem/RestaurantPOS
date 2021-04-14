from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMessage
from django.template import TemplateDoesNotExist

from app.celery import app


class Email():

    def __init__(self):
        pass

    def forget_password_email(self, user, token):

        template_name = 'authentication/reset-password.html'
        receiver = user.email
        subject = 'Resetting Your Password For ' + settings.SITE_NAME
        key = {
            'first_name': user.username,
            'password_reset_url': token
        }
        self.send_email(receiver, subject, template_name, key)

    @app.task(name='emails.activate_clipped_asset')
    def password_change_email(self, user):

        subject = 'Password Reset Successfully'
        template_name = 'authentication/reset-password-confirmation.html'
        receiver = user.email

        key = {
            'first_name': user.username
        }
        self.send_email(receiver, subject, template_name, key)

    @staticmethod
    def send_email(receiver, subject, template_name, key):

        try:

            message = get_template(template_name=template_name).render(key)
            email = EmailMessage(subject, message, to=[receiver])
            email.content_subtype = 'html'
            email.send()

        except TemplateDoesNotExist as exception:
            print(exception)
