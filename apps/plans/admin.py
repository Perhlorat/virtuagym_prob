from django.contrib import admin
from plans.models import Plan


class PlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(Plan, PlanAdmin)
