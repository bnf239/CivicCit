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
from apps.infohub.models import InfoHubUserInformation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from requests_html import HTMLSession
import json
# from .models import InfoHubUserInformation

def addUser(request):
    data = dict(request.GET)
    # print(data)
    # print("inside add users")
    # print(data["article[link]"][0])
    # print(data["article[title]"][0])
    # print(data)
    # print("---------------------")
    # print("title", ast.literal_eval((data["event"][0]))["title"])
    # print("location",ast.literal_eval((data["event"][0]))["location"])
    # print("date",ast.literal_eval((data["event"][0]))["date"] )
    # print("link",ast.literal_eval((data["event"][0]))["link"] )
    # print("------------------------------")
    # new_entry = Event(event_name=ast.literal_eval((data["event"][0]))["title"], event_location=ast.literal_eval((data["event"][0]))["location"], event_date=ast.literal_eval((data["event"][0]))["date"], event_link=ast.literal_eval((data["event"][0]))["link"])
    new_entry = InfoHubUserInformation(article_title=data["article[article]"][0], url_links = data["article[articlelink]"][0])
    new_entry.save()
    
    return render(request, "infohub/infohub.html")

def infohub_view(request):
    return render(request, "infohub/infohub.html", {})
    

def infohubtest_view(request):

    # session = HTMLSession()

    # active = []
    # api_key = '1Ms7iC-K52YCHkR70xuI_sXsZvQlHqhS3ze5DpUc_gnMm-D96G7O_GHKmu_COxuBckjlZCo7bAHkxSR1sDPMQ3lxH41VICcGlsUJPRUc1kmUrMJmROeSR4WgIQ04YnYx'

    # url = 'https://newsdata.io/api/1/news?apikey=' + api_key + '&q=political%20AND%20involvement'

    # r = session.get(url)

    # r.html.render(sleep=1)

    # finds = r.html.find('dtr-control')

    # print(finds)

    # api_key = 'pub_627591a3bd0b220ed162b624916c154861ad'


    # url = 'https://newsdata.io/api/1/news?apikey=pub_627591a3bd0b220ed162b624916c154861ad&q=political%20AND%20involvement' 
    API_key = 'ae08340bce8f4000996fc988450a02b3'
    # url = 'https://newsapi.org/v2/everything?q=(political%20AND%20involvement)&domains=nytimes.com,theguardian.com,bbc.co.uk&apiKey=ae08340bce8f4000996fc988450a02b3'
    # url = 'https://newsapi.org/v2/everything?q=(political%20AND%20involvement)&domains=nytimes.com,theguardian.com&sortBy=relevancy&apiKey=ae08340bce8f4000996fc988450a02b3'

    url = 'https://newsapi.org/v2/everything?q=(political%20AND%20involvement)&domains=nytimes.com,theguardian.com&sortBy=relevancy&apiKey=' + API_key

    # HEADERS = {'Authorization':'bearer %s' % api_key}

    # url = 'https://newsdata.io/api/1/news?apikey='+ api_key +'&q=political%20AND%20involvement'

    r = requests.get(url)

    articles = r.json()["articles"]
    # print(articles)
    # for i in data["results"]:
    #     print(i["title"])

    

    soup = BeautifulSoup(r.content, features="lxml")

    link = soup.find("results")

    # requestLink = request.POST['urlLink']
    # print("testing link:", link)
    # print(soup.get_text())

    # data = dict(request.GET)
    # print(data)

    # print(yo)

    # if request.method == 'POST':
        # print('yo')
        # userMain=request.POST.get('user', False)
        # requestLink = request.POST.get('urlLink',False)


        # new_user = InfoHubUserInformation(
        #     username = userMain,
        #     url_links = requestLink,
        # )
        # new_user.username = new_user
        # new_user.save()
        # return redirect('/')

    return render(request, "infohub/infohubtest.html", {"articles": articles})

def infohubtest2_view(request):

    # url = 'https://newsdata.io/api/1/news?apikey=pub_627591a3bd0b220ed162b624916c154861ad&q=social%20responsibility'
    API_key = 'ae08340bce8f4000996fc988450a02b3'

    url = 'https://newsapi.org/v2/everything?q=(social%20responsibility)&domains=nytimes.com,theguardian.com&sortBy=relevancy&apiKey=' + API_key

    r = requests.get(url)
    articles = r.json()["articles"]

    soup = BeautifulSoup(r.content, features="lxml")

    link = soup.find("results")

    return render(request, "infohub/infohubtest2.html", {"articles": articles})

def infohubtest3_view(request):

    # url = 'https://newsdata.io/api/1/news?apikey=pub_627591a3bd0b220ed162b624916c154861ad&q=advocacy%20AND%20education'
    API_key = 'ae08340bce8f4000996fc988450a02b3'

    url = 'https://newsapi.org/v2/everything?q=(advocacy%20AND%20education)&domains=nytimes.com,theguardian.com&sortBy=relevancy&apiKey=' + API_key

    r = requests.get(url)
    articles = r.json()["articles"]

    soup = BeautifulSoup(r.content, features="lxml")

    link = soup.find("results")

    return render(request, "infohub/infohubtest3.html", {"articles": articles})