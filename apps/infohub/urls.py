from django.urls import path, re_path, include
from apps.home import views
from .views import infohub_view, infohubtest_view, infohubtest2_view, infohubtest3_view

app_name = "infohub"

urlpatterns = [

    path('infohub/', infohub_view, name="infohub"),
    path('infohubtest/', infohubtest_view, name='infohubtest'),
    path('infohubtest2/', infohubtest2_view, name='infohubtest2'),
    path('infohubtest3/', infohubtest3_view, name='infohubtest3'),


]
