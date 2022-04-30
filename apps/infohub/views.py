from unicodedata import category
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from bs4 import BeautifulSoup
import re
import ast
import calendar
import datetime
from django.contrib.auth.models import User
from apps.infohub.models import InfoHubUserInformation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

# This function will add the article title and article link to the database for future use
def addUser(request):
    data = dict(request.GET)
    new_entry = InfoHubUserInformation(user_id=request.user.id,article_title=data["article[article]"][0], url_links = data["article[articlelink]"][0])
    new_entry.save()
    
    return render(request, "infohub/infohub.html")

# Directs to infohub.html
def infohub_view(request):
    return render(request, "infohub/infohub.html", {})
    
# For all three cases, the functions will retrieve their respective data on articles and directs user to each page with respect to that they clicked on (i.e. Political Involvement, Social Respinsibility, Educatoin and Advocacy)

def infohubtest_view(request):

    API_key = 'ae08340bce8f4000996fc988450a02b3'

    url = 'https://newsapi.org/v2/everything?q=(political%20AND%20involvement)&domains=nytimes.com,theguardian.com&sortBy=relevancy&apiKey=' + API_key

    r = requests.get(url)

    articles = r.json()["articles"]

    soup = BeautifulSoup(r.content, features="lxml")

    link = soup.find("results")

    return render(request, "infohub/infohubtest.html", {"articles": articles})

def infohubtest2_view(request):

    API_key = 'ae08340bce8f4000996fc988450a02b3'

    url = 'https://newsapi.org/v2/everything?q=(social%20responsibility)&domains=nytimes.com,theguardian.com&sortBy=relevancy&apiKey=' + API_key

    r = requests.get(url)

    articles = r.json()["articles"]

    soup = BeautifulSoup(r.content, features="lxml")

    link = soup.find("results")

    return render(request, "infohub/infohubtest2.html", {"articles": articles})

def infohubtest3_view(request):
    
    API_key = 'ae08340bce8f4000996fc988450a02b3'

    url = 'https://newsapi.org/v2/everything?q=(advocacy%20AND%20education)&domains=nytimes.com,theguardian.com&sortBy=relevancy&apiKey=' + API_key

    r = requests.get(url)

    articles = r.json()["articles"]

    soup = BeautifulSoup(r.content, features="lxml")

    link = soup.find("results")

    return render(request, "infohub/infohubtest3.html", {"articles": articles})