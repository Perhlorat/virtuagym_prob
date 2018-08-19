from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


class Plan(models.Model):

    name = models.CharField(_('Title'), max_length=255)
    users = models.ManyToManyField(User)
    datetime_created = models.DateTimeField(_('Datetime created'), auto_now_add=True)
    datetime_updated = models.DateTimeField(_('Datetime updated'), auto_now=True)

    def __str__(self):
        return self.name
