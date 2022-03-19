from unicodedata import category
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from bs4 import BeautifulSoup
from .forms import EventForm
import re
 
def returnResult(request,category,location):
    print(request)
    print(category)
    city = re.split(r', ',location.lower())[0]
    state = re.split(r', ',location.lower())[1]
    print(city)
    print(state)
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
    # headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    # url = 'https://www.meetup.com/find/events/?allMeetups=true&radius=25&userFreeform=New York, NY&mcId=c10001&mcName=New York, NY&categoryId=604'
    # response=requests.get(url,headers=headers)
    # soup=BeautifulSoup(response.content,'html')
    # events = []
    # for i in range(len(soup.find("div", { "class" : "max-w-narrow" }).find("div", { "class" : "max-w-narrow" }).contents)):
    #     try:
    #         print(soup.find("div", { "class" : "max-w-narrow" }).find("div", { "class" : "max-w-narrow" }).contents[i].select('p')[0].get_text())
    #         events.append(soup.find("div", { "class" : "max-w-narrow" }).find("div", { "class" : "max-w-narrow" }).contents[i].select('p')[0].get_text())
    #     except:
    #         pass
    #         #print(soup.find("div", { "class" : "max-w-narrow" }).find("div", { "class" : "max-w-narrow" }).contents[i].select())
    
    
    events = []
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    pageNum = 1
    url = 'https://www.eventbrite.com/d/{}--{}/{}/?page={}'.format(state,city,category,pageNum)

    response=requests.get(url,headers=headers)

    soup=BeautifulSoup(response.content,'html')

    results = soup.find_all("div",{ "class" : "search-event-card-wrapper" })
    resultNum = 1
    while len(results)>0:
        for i in range(len(results)):
            resDict = {}
            try:
                print("Title of Event:",results[i].find('div', attrs={'class': 'eds-is-hidden-accessible'}).text)
                resDict["title"] = results[i].find('div', attrs={'class': 'eds-is-hidden-accessible'}).text
            except:
                resDict["title"] = "NO DATA"
            try:
                print("Link of Event:",results[i].contents[0].select('a')[0]["href"])
                resDict["link"] = results[i].contents[0].select('a')[0]["href"]
            except:
                resDict["link"] = "NO DATA"
            try:
                print("Image of Event:",results[i].contents[0].select('img')[0]["src"])
                resDict["image"] = results[i].contents[0].select('img')[0]["src"]
            except:
                resDict["image"] = "NO DATA"
            try:
                print("Date and Time of Event:",  results[i].find("div",{ "class" : "eds-event-card-content__sub-title eds-text-color--ui-orange eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm" }).text)
                resDict["date"] =  results[i].find("div",{ "class" : "eds-event-card-content__sub-title eds-text-color--ui-orange eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm" }).text
            except:
                resDict["date"] = "NO DATA"
            events.append(resDict)
            # print(i)
            # print("-----------------",pageNum)
            resultNum+=1
        pageNum+=1
        url = 'https://www.eventbrite.com/d/{}--{}/{}/?page={}'.format(state,city,category,pageNum)
        response=requests.get(url,headers=headers)
        soup=BeautifulSoup(response.content,'html')
        results = soup.find_all("div",{ "class" : "search-event-card-wrapper" })

    
    return events
    
 
def events_view(request):
    # initial user display

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            # event = form.save(commit=False)
            location = form['location'].value()
            category = form['category'].value()
            # print(location)
            # print(category)
            events = returnResult(request,category, location)
            return render(request, "events/events.html", {"form": form, "events":events})
    form = EventForm()

    return render(request, "events/events.html", {"form": form})


