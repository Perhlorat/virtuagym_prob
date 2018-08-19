from django.utils.translation import gettext as _
from rest_framework import serializers

from plans.models import Plan
from users.serializers import PlanUserSerializer


class PlanSerializer(serializers.ModelSerializer):
    users = PlanUserSerializer(read_only=True, many=True)
    class Meta:
        model = Plan
        fields = ['id', 'name', 'users']
