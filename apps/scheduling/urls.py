from django.urls import path
from .views import scheduleEvent #deleteEvent
from django.contrib.auth.views import LogoutView
app_name = "scheduling"
urlpatterns = [
    path('scheduling/', scheduleEvent, name = "schedule_event"),
   
]
