from unicodedata import category
from django import template
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect, HttpRequest

import mimetypes
import os 


from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from bs4 import BeautifulSoup




# from .forms import EventForm
import re
import ast
import calendar
import datetime
#from django.contrib.auth.models import User
from apps.scheduling.models import Event
from apps.infohub.models import InfoHubUserInformation
from apps.quiz.models import QuizCategoryModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from requests_html import HTMLSession
import json


def addUser(request):
    data = dict(request.GET)
    # print(data)
    # print("---------------------")
    # print("title", ast.literal_eval((data["event"][0]))["title"])
    # print("location",ast.literal_eval((data["event"][0]))["location"])
    # print("date",ast.literal_eval((data["event"][0]))["date"] )
    # print("link",ast.literal_eval((data["event"][0]))["link"] )
    # print("------------------------------")
    # new_entry = Event(event_name=ast.literal_eval((data["event"][0]))["title"], event_location=ast.literal_eval((data["event"][0]))["location"], event_date=ast.literal_eval((data["event"][0]))["date"], event_link=ast.literal_eval((data["event"][0]))["link"])
    
    return render(request, "progress_report/progress_report.html")

def progress_report_view(request):
    num_events = number_of_events_registered_for(request)
    num_articles_read = number_of_articles_read(request)
    num_of_quizzes = number_of_quizzes(request)
    quiz_inform = quiz_info(request)
    print(quiz_inform)
    for data in quiz_inform:
        print(data.category)
        print(data.percent)
    context = {
        "num_events" : num_events,
        "num_articles_read" : num_articles_read,
        "num_of_quizzes" : num_of_quizzes,
        "quiz_info" : quiz_inform
    }
    return render(request, "progress_report/progress_report.html", context)


def number_of_events_registered_for(request):
    num_events = len(list(Event.objects.all().filter(event_status = True, user_id=request.user.id)))
    return num_events

def number_of_articles_read(request):
    #print(set(InfoHubUserInformation.objects.all()))
    articles = InfoHubUserInformation.objects.all().filter(user_id=request.user.id)
    
    article_links = []

    for article in articles:
        article_links.append(article.url_links)

    unique_articles = len(set(article_links))
    return unique_articles

def number_of_quizzes(request):
    num_of_quizzes = len(list(QuizCategoryModel.objects.all().filter(completed = True, user_id=request.user.id)))
    return num_of_quizzes


def quiz_info(request):
    quiz = list(QuizCategoryModel.objects.all().filter(user_id=request.user.id))
    return quiz

def download_file(request):
 # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'test.txt'
    # Define the full file path
    filepath = BASE_DIR + '/downloadapp/Files/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response



   
 



