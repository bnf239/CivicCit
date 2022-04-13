from django.urls import path, re_path, include
from apps.home import views
from .views import quiz_view, quiz1_view, quiz2_view, quiz3_view

app_name = "quiz"

urlpatterns = [

    path('quiz/', quiz_view, name="quiz"),
    path('politics/', quiz1_view, name='politics'),
    path('social_resp/', quiz2_view, name='social_resp'),
    path('service/', quiz3_view, name='service'),


]
