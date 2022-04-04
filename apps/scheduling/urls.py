from django.urls import path
from .views import scheduleEvent
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('scheduling/', scheduleEvent, name = "schedule_event"),
]
