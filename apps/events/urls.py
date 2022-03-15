from django.urls import path, re_path
from apps.home import views
from .views import events_view
 
urlpatterns = [

    path('events/', events_view, name="events")

]
