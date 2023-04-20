from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import RegexValidator


class Mail(models.Model):
    subject = models.CharField(max_length=100)
    send_to = models.CharField(max_length=100, verbose_name= ('To'))
    send_from = models.CharField(max_length=100, verbose_name= ('From'))
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    passcode = models.CharField(max_length=100, default='', blank=True,
        validators=[RegexValidator(regex='^.{8}$| ', message='The passcode must have exactly 8 characters', code='nomatch')]
    )
    nonce = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return 'From: ' + self.send_from + '\nTo: ' + self.send_to + '\nSubject: ' + self.subject

    def get_absolute_url(self):
        if(self.passcode!=''):
            return reverse('email-secret')
        else:
            return reverse('email-sent')
