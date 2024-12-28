from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    main_muscle_group = models.CharField(max_length=255)
    equipment = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Routine(models.Model):
    name = models.CharField(max_length=255)
    exercises = models.ManyToManyField(Exercise)

class Workout(models.Model):
    date = models.DateField()
    routine = models.ForeignKey(Routine, on_delete=models.SET_NULL, null=True)
    volume = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.date)

class Set(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    set_type = models.CharField(max_length=255)
    reps = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.exercise.name} - {self.reps} reps x {self.weight} kg"

class Run(models.Model):
    date = models.DateField()
    distance = models.PositiveSmallIntegerField()
    time = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.date)