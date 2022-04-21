from unicodedata import category
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
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
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import QuesModel, QuizCategoryModel

# from requests_html import HTMLSession
import json
# from .models import InfoHubUserInformation

def start(request):
    #create quiz category results rows
    results = createCategoryTable()
    context = {"results" : results}

    return render(request, "quiz/quiz.html", context)

def quiz_view(request):
    #get category from button pressed
    #post questions in multiple choice form
    #when submit button is pressed, check if the answer pressed is equal to the answer
    #if it is, then increase the number right counter
    #at the end, calculate the percentage and update the category, numRight, totalQuestions, and percentage into database
    #display category results into html table
    return render(request, "quiz/quiz.html")

def quiz1_view(request):

    return render(request, "quiz/quiz1.html", {})

def quiz2_view(request):

    return render(request, "quiz/quiz2.html", {})

def quiz3_view(request):

    return render(request, "quiz/quiz3.html", {})


def politicalquiz():
    #insert 10 questions into database
    question 

def socialquiz():
    #insert 10 questions into database
    return

def communityquiz():
    #insert 10 questions into database
    return

def createCategoryTable():
    political = QuizCategoryModel(category='P',numRight=0, totalQuestions=10, percent=100)
    political.save()
    social = QuizCategoryModel(category='S',totalQuestions=10)
    social.save()
    community = QuizCategoryModel(category='C',totalQuestions=10)
    community.save()
    categories = QuizCategoryModel.objects.all()
    return categories
