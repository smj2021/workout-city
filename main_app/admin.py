from django.contrib import admin
from .models import Workout, DidWorkout

# Register your models here
admin.site.register(Workout)
admin.site.register(DidWorkout)