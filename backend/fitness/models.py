from django.db import models

import datetime

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    main_muscle_group = models.CharField(max_length=255)
    equipment = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} ({self.equipment})'

class Routine(models.Model):
    name = models.CharField(max_length=255)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.name

class Workout(models.Model):
    date = models.DateField(default=datetime.date.today)
    routine = models.ForeignKey(Routine, on_delete=models.SET_NULL, null=True, blank=True)
    volume = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.date)

class Set(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    set_type = models.CharField(max_length=255, default='Normal')
    reps = models.PositiveSmallIntegerField()
    weight = models.FloatField(default=0)

    def __str__(self):
        return f"{self.exercise.name} - {self.reps} reps x {self.weight} kg"

class Run(models.Model):
    date = models.DateField()
    distance = models.PositiveSmallIntegerField()
    time = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.date)