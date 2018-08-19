from rest_framework import viewsets

from days.models import Day
from days.serializers import DaySerializer


class DayViewset(viewsets.ModelViewSet):
    """
    Simple restaurant REST API CRUD ViewSet
    """
    serializer_class = DaySerializer
    queryset = Day.objects.prefetch_related('exercise_set').all()
