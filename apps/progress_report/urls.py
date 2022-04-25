from django.urls import path, re_path, include
from apps.home import views
from .views import progress_report_view, number_of_events_registered_for


app_name = "progress_report"

urlpatterns = [

    path('progress_report/', progress_report_view, name="progress_report"),
    #path('infohubtest/', infohubtest_view, name='infohubtest'),
    #path('infohubtest2/', infohubtest2_view, name='infohubtest2'),
   # path('infohubtest3/', infohubtest3_view, name='infohubtest3'),


]
