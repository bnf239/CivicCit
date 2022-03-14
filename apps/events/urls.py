from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # This will be our landing/home page
    path('', views.index, name='home'),

    # matching the html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
