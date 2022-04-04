from django.urls import path, re_path, include
from apps.home import views
from apps.events.views import events_view 
from apps.infohub.views import infohub_view
from apps.scheduling.views import scheduleEvent, startup
urlpatterns = [

    # This will be our landing/home page
    path('', views.index, name='home'),
    path('events/', events_view, name="events"),
    path('infohub/', infohub_view, name="infohub"),
    path('scheduling', scheduleEvent, name="schedule_events"),
    path('scheduling/', startup, name="scheduling"),

    # matching the html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
