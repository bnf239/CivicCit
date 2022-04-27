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
from .forms import PQuizForm, SQuizForm, CQuizForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import QuizCategoryModel

# from requests_html import HTMLSession
import json
# from .models import InfoHubUserInformation

def start(request):
    #create quiz category results rows

    return render(request, "quiz/quiz.html")

def quiz_view(request):

    a1 = ''
    a2 = ''
    a3 = ''
    a4 = ''
    a5 = ''
    a6 = ''
    a7 = ''
    a8 = ''
    a9 = ''
    a10 = ''
    results = QuizCategoryModel.objects.all().filter(user_id=request.user.id)
    if not results.exists():
        results = createCategoryTable(request)
    if "Submit Political" in request.POST:
        numCorrect = 0
        form = PQuizForm(request.POST)
        if form.is_valid():
            a1 = form.cleaned_data['answers1']
            a2 = form.cleaned_data['answers2']
            a3 = form.cleaned_data['answers3']
            a4 = form.cleaned_data['answers4']
            a5 = form.cleaned_data['answers5']
            a6 = form.cleaned_data['answers6']
            a7 = form.cleaned_data['answers7']
            a8 = form.cleaned_data['answers8']
            a9 = form.cleaned_data['answers9']
            a10 = form.cleaned_data['answers10']
        
        if a1 == "to ensure citizen\'s life, liberty and property are protected":
            numCorrect = numCorrect + 1
        if a2 == "right":
            numCorrect = numCorrect + 1
        if a3 == "The Vietnam War":
            numCorrect = numCorrect + 1
        if a4 == "not voting":
            numCorrect = numCorrect + 1
        if a5 == "popular sovereignty":
            numCorrect = numCorrect + 1
        if a6 == "all of the above":
            numCorrect = numCorrect + 1
        if a7 == "the Electoral College":
            numCorrect = numCorrect + 1
        if a8 =="by contributing to election campaign funds":
            numCorrect = numCorrect + 1
        if a9 == "to influence state legislators or members of Congress on issues":
            numCorrect = numCorrect + 1
        if a10 == "the wording of the questions of the poll":
            numCorrect = numCorrect + 1

        p = QuizCategoryModel.objects.filter(user_id=request.user.id).get(category='P')
        p.completed = True
        p.save()
        p.numRight = numCorrect
        p.save()
        p.percent = (numCorrect / p.totalQuestions) * 100
        p.save()
        results = list(QuizCategoryModel.objects.all().filter(user_id=request.user.id).order_by('id'))
    if "Submit Social" in request.POST:
        numCorrect = 0
        form = SQuizForm(request.POST)
        if form.is_valid():
            a1 = form.cleaned_data['answers1']
            a2 = form.cleaned_data['answers2']
            a3 = form.cleaned_data['answers3']
            a4 = form.cleaned_data['answers4']
            a5 = form.cleaned_data['answers5']
            a6 = form.cleaned_data['answers6']
            a7 = form.cleaned_data['answers7']
            a8 = form.cleaned_data['answers8']
            a9 = form.cleaned_data['answers9']
            a10 = form.cleaned_data['answers10']
        
        if a1 == "donating blood":
            numCorrect = numCorrect + 1
        if a2 == "paying taxes":
            numCorrect = numCorrect + 1
        if a3 == "produce responsible citizens and active participants in community and government":
            numCorrect = numCorrect + 1
        if a4 == "attending school until your state\'s compulsory attendance age is reached":
            numCorrect = numCorrect + 1
        if a5 == "registering to vote":
            numCorrect = numCorrect + 1
        if a6 == "go to school":
            numCorrect = numCorrect + 1
        if a7 == "exercising and eating healthy":
            numCorrect = numCorrect + 1
        if a8 == "being a member of a nation or country and having full rights and responsibilities under the law":
            numCorrect = numCorrect + 1
        if a9 == "civic duties are required but civic responsibilities are optional":
            numCorrect = numCorrect + 1
        if a10 == "it provides the best opportunity for a fair trial of your peers":
            numCorrect = numCorrect + 1

        s = QuizCategoryModel.objects.filter(user_id=request.user.id).get(category='S')
        s.completed = True
        s.save()
        s.numRight = numCorrect
        s.save()
        s.percent = (numCorrect / s.totalQuestions) * 100
        s.save()
        results = list(QuizCategoryModel.objects.all().filter(user_id=request.user.id).order_by('id'))
    if "Submit Community" in request.POST: 
        numCorrect = 0
        form = CQuizForm(request.POST)
        if form.is_valid():
            a1 = form.cleaned_data['answers1']
            a2 = form.cleaned_data['answers2']
            a3 = form.cleaned_data['answers3']
            a4 = form.cleaned_data['answers4']
            a5 = form.cleaned_data['answers5']
            a6 = form.cleaned_data['answers6']
            a7 = form.cleaned_data['answers7']
            a8 = form.cleaned_data['answers8']
            a9 = form.cleaned_data['answers9']
            a10 = form.cleaned_data['answers10']
        
        if a1 == "volunteering to do free work to benefit your community":
            numCorrect = numCorrect + 1
        if a2 == "all of the above":
            numCorrect = numCorrect + 1
        if a3 == "volunteer to work with a group that cleans the city park":
            numCorrect = numCorrect + 1
        if a4 == "all of the above":
            numCorrect = numCorrect + 1
        if a5 == "by volunteerism and civic responsibility":
            numCorrect = numCorrect + 1
        if a6 == "ethics":
            numCorrect = numCorrect + 1
        if a7 == "volunteering":
            numCorrect = numCorrect + 1
        if a8 == "policy change":
            numCorrect = numCorrect + 1
        if a9 == "all of the above":
            numCorrect = numCorrect + 1
        if a10 == "something done that does not benefit anyone":
            numCorrect = numCorrect + 1

        c = QuizCategoryModel.objects.filter(user_id=request.user.id).get(category='C')
        c.completed = True
        c.save()
        c.numRight = numCorrect
        c.save()
        c.percent = (numCorrect / c.totalQuestions) * 100
        c.save()
        results = list(QuizCategoryModel.objects.all().filter(user_id=request.user.id).order_by('id'))
    context = {"results" : results}
    return render(request, "quiz/quiz.html", context)
    
def quiz1_view(request):
    context = {}
    context['form'] = PQuizForm()
    return render(request, "quiz/quiz1.html", context)

def quiz2_view(request):
    context = {}
    context['form'] = SQuizForm()
    return render(request, "quiz/quiz2.html", context)

def quiz3_view(request):
    context = {}
    context['form'] = CQuizForm()
    return render(request, "quiz/quiz3.html", context)



def createCategoryTable(request):
    print(request.user.id)
    political = QuizCategoryModel(user_id= request.user.id,category='P', totalQuestions=10)
    political.save()
    social = QuizCategoryModel(user_id=request.user.id, category='S',totalQuestions=10)
    social.save()
    community = QuizCategoryModel(user_id=request.user.id, category='C',totalQuestions=10)
    community.save()
    categories = list(QuizCategoryModel.objects.all().filter(user_id=request.user.id).values())
    return categories
