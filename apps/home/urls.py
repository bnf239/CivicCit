from django.urls import path, re_path, include
from apps.home import views
from apps.events.views import events_view 
from apps.infohub.views import infohub_view, infohubtest_view, infohubtest2_view
from apps.scheduling.views import scheduleEvent, startup, deleteEvent
urlpatterns = [

    # This will be our landing/home page
    path('', views.index, name='home'),
    path('events/', events_view, name="events"),
    path('infohub/', infohub_view, name="infohub"),
    path('infohubtest/', infohubtest_view, name="infohubtest"),
    path('infohubtest2/', infohubtest2_view, name="infohubtest2"),
    path('scheduling', scheduleEvent, name="schedule_events"),
    path('scheduling/', startup, name="scheduling"),
    path('scheduling/delete_event/(?P<event_id>\d+)',deleteEvent,name="delete_event"),
     path('scheduling/delete_event/',deleteEvent,name="delete_event"),

    # matching the html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]

