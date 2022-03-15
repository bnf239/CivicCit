from django.urls import path, re_path
from apps.home import views
from apps.events.views import events_view
urlpatterns = [

    # This will be our landing/home page
    path('', views.index, name='home'),
    path('events/', events_view, name="events"),

    # matching the html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
