from django.urls import path, re_path, include
from apps.home import views
from apps.events.views import events_view 
from apps.infohub.views import infohub_view, infohubtest_view, infohubtest2_view, infohubtest3_view, addUser
from apps.scheduling.views import scheduleEvent, startup, deleteEvent, registerEvent
from apps.quiz.views import start, quiz_view, quiz1_view, quiz2_view, quiz3_view
from apps.progress_report.views import progress_report_view
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
    path('scheduling/register_event/',registerEvent,name="register_event"),
    # path('scheduling/',deleteEvent,name="delete_event"),
    path('quiz', start, name="quizhome"),
    path('quiz/', quiz_view, name="quiz"),
    path('political_involvement/', quiz1_view, name='political_involvement'),
    path('social_responsibility/', quiz2_view, name='social_responsibility'),
    path('community_service/', quiz3_view, name='community_service'),
    path('scheduling/delete_event/',deleteEvent,name="delete_event"),
    # path(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    path('progress_report', progress_report_view, name = 'progress_report'),

    # matching the html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]

