from django.contrib import admin
from days.models import Day


class DayAdmin(admin.ModelAdmin):
    pass


admin.site.register(Day, DayAdmin)
