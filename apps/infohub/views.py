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
import calendar
import datetime
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from requests_html import HTMLSession


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


    url = 'https://newsdata.io/api/1/news?apikey=pub_627591a3bd0b220ed162b624916c154861ad&q=political%20AND%20involvement' 

    # HEADERS = {'Authorization':'bearer %s' % api_key}

    # url = 'https://newsdata.io/api/1/news?apikey='+ api_key +'&q=political%20AND%20involvement'

    r = requests.get(url)

    articles = r.json()["results"]
    # for i in data["results"]:
    #     print(i["title"])

    

    soup = BeautifulSoup(r.content, features="lxml")

    link = soup.find("results")

    # print("testing link:", link)
    # print(soup.get_text())

    return render(request, "infohub/infohubtest.html", {"articles": articles})

def infohubtest2_view(request):

    url = 'https://newsdata.io/api/1/news?apikey=pub_627591a3bd0b220ed162b624916c154861ad&q=social%20responsibility'

    r = requests.get(url)
    articles = r.json()["results"]

    soup = BeautifulSoup(r.content, features="lxml")

    link = soup.find("results")

    return render(request, "infohub/infohubtest2.html", {"articles": articles})