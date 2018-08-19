from django.db import models
from django.utils.translation import gettext as _

from days.models import Day


class Exercise(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    name = models.CharField(_('Exercise name'), max_length=255)

    datetime_created = models.DateTimeField(_('Datetime created'), auto_now_add=True)
    datetime_updated = models.DateTimeField(_('Datetime created'), auto_now=True)

    def __str__(self):
        data = {
            'day': str(self.day),
            'name': self.name
        }
        return 'Day {day} exercise: {name}'.format(**data)
