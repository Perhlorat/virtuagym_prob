from rest_framework import viewsets

from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer


class ExerciseViewset(viewsets.ModelViewSet):
    """
    Simple restaurant REST API CRUD ViewSet
    """
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()
