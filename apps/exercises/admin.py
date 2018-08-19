from django.contrib import admin
from exercises.models import Exercise


class ExerciseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Exercise, ExerciseAdmin)
