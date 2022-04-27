from unicodedata import category
from django import template
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import HttpResponse, StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os 
from io import StringIO
import pdfkit as pdf
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from bs4 import BeautifulSoup
from reportlab.pdfgen.canvas import Canvas
from io import BytesIO
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm
from django.contrib.auth.models import User




# from .forms import EventForm
import re
import ast
import calendar
import datetime
#from django.contrib.auth.models import User
from apps.scheduling.models import Event
from apps.infohub.models import InfoHubUserInformation
from apps.quiz.models import  QuizCategoryModel
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

# def download_file(request):
#     print("inside download file")
#     instance = Event.objects.all()
    
#     html_file = render_to_string('progress_report/progress_report.html', {'instance':instance})

#     filename = f'something.pdf'
#     canvas = Canvas("hello.pdf")
#     canvas.drawString(72, 72, "Hello, World")
#     canvas.save()

#     content = canvas

#     response = HttpResponse(content, headers={
#     'Content-Type': 'application/pdf',
#     'Content-Disposition': f'attachment; filename="{filename}"' })

#     return response

def create_pdf(request):
    buffer = BytesIO()
    canvas = Canvas(buffer, pagesize=A4)
    WIDTH, HEIGHT = A4
    MARIGIN = 1.5 * cm
    canvas.translate(MARIGIN, HEIGHT-MARIGIN)
    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
    pdfmetrics.registerFont(TTFont('Verabd', 'Verabd.ttf'))

    # header
    canvas.setFont("Verabd", size=14)
    canvas.drawString(160, 0, "Progress Report")
    canvas.setFont("Vera", size=10)
    canvas.drawString(430, -0.9*cm, "Username: "+str(request.user.username))
    canvas.setStrokeGray(0)
    canvas.line(0, -1*cm, WIDTH - 2*MARIGIN, -1*cm)

    # footer
    canvas.line(0, -26.6*cm, WIDTH - 2*MARIGIN, -26.6*cm)
    articles = number_of_articles_read(request)
    events = number_of_events_registered_for(request)
    quizzes = number_of_quizzes(request)


    # paragraphs
    txt_obj = canvas.beginText(14, -6.5* cm)
    txt_obj.setFont("Vera", 12)
    txt_obj.setWordSpace(3)
    txt_lst = ["Number of Quizzes Completed: "+ str(quizzes), 
                "Total Events Registered For: "+ str(events),
                "Articles Read: " + str(articles)  ,
                ]
    for line in txt_lst:
        txt_obj.textOut(line)
        txt_obj.moveCursor(0, 16)
    canvas.drawText(txt_obj)


    canvas.showPage()
    canvas.save()
    return buffer

def download_file(request):

    pdf = create_pdf(request)
    pdf.seek(0)

    response = HttpResponse(pdf, headers={
    'Content-Type': 'application/pdf',
    'Content-Disposition': 'attachment; filename="{}_progress_report.pdf"'.format(str(request.user.username)) })

    return response

   
 



