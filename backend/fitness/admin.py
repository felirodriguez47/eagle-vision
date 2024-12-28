from django.contrib import admin

from .models import Exercise, Routine, Workout, Set, Run
# Register your models here.

admin.site.register(Exercise)
admin.site.register(Routine)
admin.site.register(Workout)
admin.site.register(Set)
admin.site.register(Run)