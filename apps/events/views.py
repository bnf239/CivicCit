from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from bs4 import BeautifulSoup

 
def events_view(request):
    # complete logic here
    url = "https://www.imdb.com/chart/moviemeter/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find('table',  {'class': 'chart full-width'})
    rows = table.find_all('tr')
    movies = []
    for row in rows:
        image = row.find('img')
        if image:
            movies.append(image['alt'])
    return render(request, "events/events.html", {'movies': movies})
 