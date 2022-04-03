from django.urls import path, re_path, include
from apps.home import views
from apps.events.views import infohub_view

app_name = "infohub"

urlpatterns = [

    path('infohub/', infohub_view, name="infohub"),


]
