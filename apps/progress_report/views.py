from cgitb import text
from turtle import down
from unicodedata import category
from django import template
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, StreamingHttpResponse

from django.shortcuts import render 
from io import BytesIO
from django.template.loader import get_template
from django.views import View 
from xhtml2pdf import pisa 

import mimetypes
import os
from wsgiref.util import FileWrapper

from django.template import loader
from django.shortcuts import redirect
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
    print("im here")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = "test.pdf"
    filepath = base_dir + '/Files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile, 'r'), chunk_size), 
        content_type = mimetypes.guess_type(thefile[0]))
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment;filename=%s" % filename
    return render(request, "progress_report/progress_report.html", response)
















   

    
  








   
 



