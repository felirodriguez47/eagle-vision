from rest_framework import serializers
from .models import Exercise, Workout, Routine, Set

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = '__all__'

class SetSerializer(serializers.ModelSerializer):
    exercise_name = serializers.CharField(source='exercise.name', read_only=True)

    class Meta:
        model = Set
        fields = ['id', 'exercise_name', 'set_type','reps', 'weight'] 

class WorkoutSerializer(serializers.ModelSerializer):
    sets = SetSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'date', 'routine', 'volume', 'sets']