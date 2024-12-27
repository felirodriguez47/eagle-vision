from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'gym/exercises', views.ExerciseViewSet)
router.register(r'gym/workouts', views.WorkoutViewSet)
router.register(r'gym/sets', views.SetViewSet)
# router.register(r'running/runs', running_views.RunViewSet)  # Add running URLs later

urlpatterns = [
    path('', include(router.urls)),
]