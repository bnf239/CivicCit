from django.urls import path, re_path, include
from apps.home import views
from .views import quiz_view, quiz1_view, quiz2_view, quiz3_view

app_name = "quiz"

urlpatterns = [

    path('quiz/', quiz_view, name="quiz"),
    path('quiz1/', quiz1_view, name='quiz1'),
    path('quiz2/', quiz2_view, name='quiz2'),
    path('quiz3/', quiz3_view, name='quiz3'),


]
