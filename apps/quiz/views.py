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
from .models import QuesModel, QuizCategoryModel

# from requests_html import HTMLSession
import json
# from .models import InfoHubUserInformation

def start(request):
    #create quiz category results rows

    return render(request, "quiz/quiz.html")

def quiz_view(request):
    politicalquiz()
    socialquiz()
    communityquiz()

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
        
        questions = list(QuesModel.objects.filter(category='P'))
        for i in range(len(questions)):
            if a1 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a2 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a3 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a4 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a5 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a6 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a7 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a8 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a9 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a10 == questions[i].ans:
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
        
        questions = list(QuesModel.objects.filter(category='S'))
        for i in range(len(questions)):
            if a1 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a2 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a3 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a4 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a5 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a6 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a7 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a8 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a9 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a10 == questions[i].ans:
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
        
        questions = list(QuesModel.objects.filter(category='C'))
        for i in range(len(questions)):
            if a1 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a2 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a3 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a4 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a5 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a6 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a7 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a8 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a9 == questions[i].ans:
                numCorrect = numCorrect + 1
            if a10 == questions[i].ans:
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

def politicalquiz():
    #insert 10 questions into database
    q1 = QuesModel(question="Why is it required for all American citizens to obey the law?", category='P', op1="to ensure citizen\'s life, liberty and property are protected", op2="to ensure all Americans are treated equally", op3="to ensure an executive order is approved by Congress", op4="to ensure enough funds are collected in speeding tickets to fund the police", ans="to ensure citizen\'s life, liberty and property are protected")
    q1.save()
    q2 = QuesModel(question="Voting in the US is legally a:", category='P', op1="right", op2="obligation", op3="duty", op4="burden", ans="right")
    q2.save()
    q3 = QuesModel(question="When was the last time the draft was enacted in the United States?", category='P', op1="The Vietnam War", op2="The Persian Gulf War", op3="Korean War", op4="World War II", ans="The Vietnam War")
    q3.save()
    q4 = QuesModel(question="Which of the following is legally permitted?", category='P', op1="men not registering for the Selective Service at age 18", op2="dropping out of high school in Missouri when you are 15 years old", op3="not voting", op4="tax evasion", ans="not voting")
    q4.save()
    q5 = QuesModel(question="The right to vote best relates to which Constitutional principle?", category='P', op1="judicidal review", op2="checks and balances", op3="separation of powers", op4="popular sovereignty", ans="popular sovereignty")
    q5.save()
    q6 = QuesModel(question="What does the Constitution do?", category='P', op1="sets up the government", op2="defines the government", op3="protects the basic rights of Americans", op4="all of the above", ans="all of the above")
    q6.save()
    q7 = QuesModel(question="Which group actually picks the Presidential winner based on the popular vote?", category='P', op1="the governors of each state", op2="the US senate", op3="the US house of representatives", op4="the Electoral College", ans="the Electoral College")
    q7.save()
    q8 = QuesModel(question="Which of the following is not one of the ways in which the media affects politics?", category='P', op1="by providing information on both parties", op2="by contributing to election campaign funds", op3="by focusing public attention on particular issues", op4="by providing in-depth coverage of national news", ans="by contributing to election campaign funds")
    q8.save()
    q9 = QuesModel(question="Which best describes the main objective of a lobbyist?", category='P', op1="to raise campaign funds for political parties", op2="to influence public decision-making for the common good", op3="to influence state legislators or members of Congress on issues", op4="to advise political candidates on how to manage their election campaigns", ans="to influence state legislators or members of Congress on issues")
    q9.save()
    q10 = QuesModel(question="The validity of public opinion polls may be affected by several factors including:", category='P', op1="excessing polling", op2="poll overrepresentation of political culture factors such as liberty and civic duty", op3="overrepresentation of the views of the elite", op4="the wording of the questions of the poll", ans="the wording of the questions of the poll")
    q10.save()
    questions = list(QuesModel.objects.all())
    return questions

def socialquiz():
    #insert 10 questions into database
    q1 = QuesModel(question="Which of the following is the best example of civic responsibility?", category='S', op1="attending school", op2="jury duty", op3="going to work", op4="donating blood", ans="donating blood")
    q1.save()
    q2 = QuesModel(question="All of the following are civic responsibilities except:", category='S', op1="holding elected office", op2="registering to vote", op3="respecting other people\'s opinions", op4="paying taxes", ans="paying taxes")
    q2.save()
    q3 = QuesModel(question="Schools teach civic responsibility to students with the goal to:", category='S', op1="produce responsible citizens and active participants in community and government", op2="ensure everyone will run for an elected office", op3="ensure everyone pays their taxes on time", op4="produce citizens who will serve in the military", ans="produce responsible citizens and active participants in community and government")
    q3.save()
    q4 = QuesModel(question="Which is an example of a required civic responsibility?", category='S', op1="serving in the military", op2="communicating with government officials", op3="going to college", op4="attending school until your state’s compulsory attendance age is reached", ans="attending school until your state\'s compulsory attendance age is reached")
    q4.save()
    q5 = QuesModel(question="Which of the following is an example of civic responsibility", category='S', op1="registering to vote", op2="going to work", op3="paying taxes", op4="attending school", ans="registering to vote")
    q5.save()
    q6 = QuesModel(question="What is a civic duty that children perform every day?", category='S', op1="listen to and obey their parents", op2="go to school", op3="sit on juries", op4="volunteer in their community", ans="go to school")
    q6.save()
    q7 = QuesModel(question="What is one example of personal responsibility?", category='S', op1="exercising and eating healthy", op2="voting", op3="running for political office", op4="obeying laws", ans="exercising and eating healthy")
    q7.save()
    q8 = QuesModel(question="What is citizenship?", category='S', op1="something that is given automatically when a person moves to a different country", op2="being a member of a nation or country and having full rights and responsibilities under the law", op3="that other grade on your report card that nobody really looks at", op4="a large boat that only carries passengers that are members of a certain country", ans="being a member of a nation or country and having full rights and responsibilities under the law")
    q8.save()
    q9 = QuesModel(question="What is the difference between a civic duty and a civic responsibility?", category='S', op1="civic duties are optional but responsibilities are required", op2="there is no difference and the words are used interchangeably", op3="civic duties are required but civic responsibilities are optional", op4="none of the answers are correct", ans="civic duties are required but civic responsibilities are optional")
    q9.save()
    q10 = QuesModel(question="Why is jury duty a civic duty?", category='S', op1="it provides the best opportunity for a fair trial of your peers", op2="it ensures that 12 people serve on every jury", op3="it ensures we have a pool of citizens to pick from", op4="it guarantees a correct verdict every time", ans="it provides the best opportunity for a fair trial of your peers")
    q10.save()
    questions = list(QuesModel.objects.all())
    return questions

def communityquiz():
    #insert 10 questions into database
    q1 = QuesModel(question="What is community service?", category='C', op1="getting paid to do a job", op2="volunteering to do something for your family", op3="volunteering to do free work to benefit your community", op4="getting compensated to do work", ans="volunteering to do free work to benefit your community")
    q1.save()
    q2 = QuesModel(question="Examples of volunteer work would be:", category='C', op1="serving in a community diner for the poor/in need", op2="picking up trash along the highway", op3="organizing a clothing drive for the less fortunate", op4="all of the above", ans="all of the above")
    q2.save()
    q3 = QuesModel(question="What could Maria do if she wanted to serve her community?", category='C', op1="buy a ticket for the fair in her town", op2="read a book on the history of her community", op3="volunteer to work with a group that cleans the city park", op4="sell lemonade in her neighborhood", ans="volunteer to work with a group that cleans the city park")
    q3.save()
    q4 = QuesModel(question="Benefits of volunteering can be:", category='C', op1="better community", op2="better self-worth", op3="learning new skills", op4="all of the above", ans="all of the above")
    q4.save()
    q5 = QuesModel(question="How do citizens contribute to the improvement of a community?", category='C', op1="by volunteerism and civic responsibility", op2="by virtue and law", op3="by following volunteerism laws", op4="by spending time at the public library", ans="by volunteerism and civic responsibility")
    q5.save()
    q6 = QuesModel(question="Which term is defined as a theory or system of moral values dealing with what is good and bad with moral duty and obligation?", category='C', op1="ethics", op2="service learning", op3="integrity", op4="productivity", ans="ethics")
    q6.save()
    q7 = QuesModel(question="What do we call it when someone works to help others by giving their time and talents without receiving pay?", category='C', op1="performing a public requirement", op2="voting", op3="volunteering", op4="acting on behalf of the constitution", ans="volunteering")
    q7.save()
    q8 = QuesModel(question="Which of the following involves designing laws, rules, protocols, and procedures to guide or influence behavior?", category='C', op1="social change", op2="economic change", op3="policy change", op4="regulation change", ans="policy change")
    q8.save()
    q9 = QuesModel(question="What is the purpose of community involvement?", category='C', op1="to increase your awareness of community needs", op2="to identify with your community", op3=" to learn to make a difference in your community", op4="all of the above", ans="all of the above")
    q9.save()
    q10 = QuesModel(question="Which of the following do not describe community service correctly?", category='C', op1="often done near the area where you live so your own community reaps the benefits of your work", op2="you do not get paid to perform community service", op3="something done that does not benefit anyone", op4="work done by a person or group of people that benefits others", ans="something done that does not benefit anyone")
    q10.save()
    questions = list(QuesModel.objects.all())
    return questions
    
def quiz1_view(request):
    politicalquiz()
    context = {}
    context['form'] = PQuizForm()
    return render(request, "quiz/quiz1.html", context)

def quiz2_view(request):
    socialquiz()
    context = {}
    context['form'] = SQuizForm()
    return render(request, "quiz/quiz2.html", context)

def quiz3_view(request):
    communityquiz()
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
    categories = list(QuizCategoryModel.objects.all().values())
    return categories
