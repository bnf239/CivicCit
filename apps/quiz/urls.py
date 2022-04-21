from django.urls import path, re_path, include
from apps.home import views
from .views import start, quiz_view, quiz1_view, quiz2_view, quiz3_view

app_name = "quiz"

urlpatterns = [

    path('quiz', start, name="quizhome"),
    path('quiz/', quiz_view, name="quiz"),
    path('political_involvement/', quiz1_view, name='political_involvement'),
    path('social_responsibility/', quiz2_view, name='social_responsibility'),
    path('community_service/', quiz3_view, name='community_service')

]
