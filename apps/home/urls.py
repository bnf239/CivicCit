from django.urls import path, re_path, include
from apps.home import views
from apps.events.views import events_view 
from apps.infohub.views import infohub_view, infohubtest_view, infohubtest2_view, infohubtest3_view, addUser
from apps.scheduling.views import scheduleEvent, startup, deleteEvent
<<<<<<< HEAD
from apps.quiz.views import quiz_view, quiz1_view, quiz2_view, quiz3_view
=======
from apps.progress_report.views import progress_report_view
>>>>>>> f3c870583f2044da95e3bf3e244ab37fef954d4e
urlpatterns = [

    # This will be our landing/home page
    path('', views.index, name='home'),
    path('events/', events_view, name="events"),
    path('infohub/', infohub_view, name="infohub"),
    path('infohubtest/', infohubtest_view, name="infohubtest"),
    path('infohubtest2/', infohubtest2_view, name="infohubtest2"),
    path('infohubtest3/', infohubtest3_view, name="infohubtest3"),
    path('infohub', addUser, name="add_user"),
    path('scheduling', scheduleEvent, name="schedule_events"),
    path('scheduling/', startup, name="scheduling"),
    path('scheduling/delete_event/(?P<event_id>\d+)',deleteEvent,name="delete_event"),
<<<<<<< HEAD
     path('scheduling/delete_event/',deleteEvent,name="delete_event"),
    path('quiz/', quiz_view, name="quiz"),
    path('politics/', quiz1_view, name='politics'),
    path('social_resp/', quiz2_view, name='social_resp'),
    path('service/', quiz3_view, name='service'),
=======
    path('scheduling/delete_event/',deleteEvent,name="delete_event"),
>>>>>>> f3c870583f2044da95e3bf3e244ab37fef954d4e
    # path(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    path('progress_report', progress_report_view, name = 'progress_report'),

    # matching the html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]

