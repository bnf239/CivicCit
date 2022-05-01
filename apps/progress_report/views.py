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
from reportlab.platypus import Table
from reportlab.lib import colors
from textwrap import wrap

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
from reportlab.platypus import SimpleDocTemplate
from io import BytesIO
from reportlab.platypus import Paragraph, Spacer
from reportlab.platypus import PageBreak, Table
from reportlab.lib.units import mm, inch
from reportlab.lib.styles import getSampleStyleSheet



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
    events = registeredEvents(request)
    article_list = articlesRead(request)

    for data in quiz_inform:
        print(data.category)
        print(data.percent)
    context = {
        "num_events" : num_events,
        "num_articles_read" : num_articles_read,
        "num_of_quizzes" : num_of_quizzes,
        "quiz_info" : quiz_inform,
        "events":events,
        "article_list": article_list

    }
    return render(request, "progress_report/progress_report.html", context)
def registeredEvents(request):
    return list(Event.objects.all().filter(event_status = True, user_id=request.user.id))

def articlesRead(request):
    articles = InfoHubUserInformation.objects.all().filter(user_id=request.user.id)
    
    article_list = []

    for article in articles:
        articleDict= {}
        try:
            articleDict[article.article_title]
        except:
            articleDict[article.article_title] = article.url_links
        article_list.append(articleDict)


    return article_list

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



def create_pdf(request):
    
    sample_style_sheet = getSampleStyleSheet()
    # if you want to see all the sample styles, this prints them
    sample_style_sheet.list()
    pdf_buffer = BytesIO()
    my_doc = SimpleDocTemplate(pdf_buffer,title='{}_progress_report.pdf'.format(str(request.user.username)))
    num_articles = number_of_articles_read(request)
    num_events = number_of_events_registered_for(request)
    num_quizzes = number_of_quizzes(request)
    articles = list(InfoHubUserInformation.objects.all().filter(user_id=request.user.id))
    quiz_inform = list(QuizCategoryModel.objects.all().filter(user_id=request.user.id))
    events = list(Event.objects.all().filter(event_status = True, user_id=request.user.id))
    flowables = []
    flowables.append(Paragraph("Progress Report", sample_style_sheet['Heading1']))
    flowables.append(Paragraph(
        "Username: "+str(request.user.username),
        sample_style_sheet['BodyText']
    ))
    flowables.append(Paragraph("Statistics", sample_style_sheet["Heading2"]))
    
    
    flowables.append(Paragraph(
        "Number of Quizzes Completed: "+ str(num_quizzes), 
        sample_style_sheet['Normal']
    ))
    flowables.append(Paragraph(
         "Total Events Registered For: "+ str(num_events),
        sample_style_sheet['Normal']
    ))
    flowables.append(Paragraph(
          "Articles Read: " + str(num_articles)  ,
        sample_style_sheet['Normal']
    ))
   
    flowables.append(Paragraph("Articles Read", sample_style_sheet["Heading2"]))
    article_data= []
    article_data.append(["Article Name","Article Link"])
    rowsHarticle = [10] 
    for article in articles:
        article_data.append([(Paragraph(article.article_title,sample_style_sheet["Normal"])),(Paragraph(article.url_links,sample_style_sheet["Normal"]))])
        rowsHarticle.append(50)
    t=Table(article_data,colWidths=200, rowHeights=rowsHarticle)

    flowables.append(t)
    flowables.append(Paragraph("Events Registered For", sample_style_sheet["Heading2"]))
    event_data= []
    event_data.append(["Event Name","Event Date","Event Location","Event URL"])
    rowsH = [10] 
    for event in events:
        event_data.append([Paragraph(event.event_name,sample_style_sheet["Normal"]),Paragraph(str(event.event_date),sample_style_sheet["Normal"]),Paragraph(event.event_location,sample_style_sheet["Normal"]),Paragraph(event.event_link,sample_style_sheet["Normal"])])
        rowsH.append(95)
   
    te=Table(event_data,colWidths=100, rowHeights=rowsH)
    flowables.append(te)
    flowables.append(Paragraph("Quizzes", sample_style_sheet["Heading2"]))
    quiz_data = []
    quiz_data.append(["Quiz Category","Quiz Grade"])
    for quiz in quiz_inform:
        cat = quiz.category
        if (cat == "P"):
            cat= "Political Involvement"
        elif(cat=="S"):
            cat = "Social Responsibility"
        elif(cat=="C"):
            cat = "Community Service"
        quiz_data.append([Paragraph(cat, sample_style_sheet["Normal"]),Paragraph(str(quiz.percent),sample_style_sheet["Normal"])])
    tq=Table(quiz_data)

    flowables.append(tq)


    my_doc.build(flowables)
    
    flowables.append(PageBreak())
   
    pagesize = (140 * mm, 216 * mm)  # width, height
    my_doc = SimpleDocTemplate(
        pdf_buffer,
        pagesize=pagesize
    )
    pdf_value = pdf_buffer.getvalue()
    pdf_buffer.close()
    return pdf_value



def download_file(request):


    pdf_value = create_pdf(request)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}_progress_report.pdf"'.format(str(request.user.username))
    
    response.write(pdf_value)
    return response

   
 



