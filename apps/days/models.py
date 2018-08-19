from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext as _

from plans.models import Plan


class Day(models.Model):
    number = models.IntegerField(_('Number of day'), default=1, validators=[MinValueValidator(1)])
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    datetime_created = models.DateTimeField(_('Datetime created'), auto_now_add=True)
    datetime_updated = models.DateTimeField(_('Datetime updated'), auto_now=True)

    def __str__(self):
        data = {
            'plan': self.plan.name,
            'day': self.number,
        }
        return '{plan}: Day number {day'.format(**data)
