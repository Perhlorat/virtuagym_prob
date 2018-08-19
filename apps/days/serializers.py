from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from days.models import Day
from exercises.serializers import ExerciseSerializer


class DaySerializer(serializers.ModelSerializer):

    exercises = serializers.SerializerMethodField()

    def get_exercises(self, obj):
        return ExerciseSerializer(instance=obj.exercise_set, many=True).data

    def validate(self, data):
        another_day = Day.objects.filter(plan=data['plan'], number=data['number'])
        if self.instance:
            another_day = another_day.exclude(id=self.instance.id)

        if another_day.exists():
            raise ValidationError('Day already exists')
        return data

    class Meta:
        model = Day
        fields = '__all__'
