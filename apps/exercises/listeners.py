from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import pre_save
from django.dispatch import receiver

from days.models import Day
from exercises.models import Exercise
from plans.models import Plan


@receiver(pre_save, sender=Plan, dispatch_uid='plan_post_save')
@receiver(pre_save, sender=Day, dispatch_uid='day_post_save')
@receiver(pre_save, sender=Exercise, dispatch_uid='exercise_post_save')
def exercise_post_save_handler(sender, instance, **kwargs):

    if instance.id:
        plan = None
        if isinstance(instance, Exercise):
            plan = instance.day.plan
        elif isinstance(instance, Day):
            plan = instance.plan
        else:
            plan = instance
        users = plan.users.all()
        for user in users:
            if user.email:
                send_mail(
                    'Your exercise changed',
                    'Your exercise changed',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=True,
                )