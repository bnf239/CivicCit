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
    # url = "https://www.imdb.com/chart/moviemeter/"
    # response = requests.get(url)
    # soup = BeautifulSoup(response.content, "html.parser")
    # table = soup.find('table',  {'class': 'chart full-width'})
    # rows = table.find_all('tr')
    # movies = []
    # for row in rows:
    #     image = row.find('img')
    #     if image:
    #         movies.append(image['alt'])
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    url = 'https://www.meetup.com/find/events/?allMeetups=true&radius=25&userFreeform=New York, NY&mcId=c10001&mcName=New York, NY&categoryId=604'
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,'html')
    events = []
    for i in range(len(soup.find("div", { "class" : "max-w-narrow" }).find("div", { "class" : "max-w-narrow" }).contents)):
        try:
            print(soup.find("div", { "class" : "max-w-narrow" }).find("div", { "class" : "max-w-narrow" }).contents[i].select('p')[0].get_text())
            events.append(soup.find("div", { "class" : "max-w-narrow" }).find("div", { "class" : "max-w-narrow" }).contents[i].select('p')[0].get_text())
        except:
            pass
            #print(soup.find("div", { "class" : "max-w-narrow" }).find("div", { "class" : "max-w-narrow" }).contents[i].select())
    
    htmlTemplate = loader.get_template('home/events.html' )
    return HttpResponse(htmlTemplate.render({'events': events}, request))
    #return render(request, "home/events.html", {'events': events})
 