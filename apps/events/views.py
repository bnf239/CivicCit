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
import calendar
import datetime
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.views.generic import View



def validate(dateString):
    if(len(dateString)==0):
        return "NO DATA"
    else:
        dateString = dateString.split(',')
        date = dateString[1].strip()+' 2022'
        time = (re.findall(r".*(?:PM|AM)", dateString[2].strip()))[0]
        newDate = date + '  ' + time
        dtobject = datetime.strptime(newDate, '%b %d %Y %I:%M %p')
        return str(dtobject)


def index(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    print("INSIDE INDEXXXX")
    return render(request, "events/events.html", {"events":events})

def returnResult(request,category,city,state):
    city =city.lower()
    state = state.lower()
    events = []
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    pageNum = 1
    date = datetime.utcnow()
    utc_time = calendar.timegm(date.utctimetuple())

    if (category != "lectures-books"):
        url = 'https://www.eventbrite.com/d/{}--{}/{}/?page={}'.format(state,city,category,pageNum)

        response=requests.get(url,headers=headers)

        soup=BeautifulSoup(response.content,'html')

        results = soup.find_all("div",{ "class" : "search-event-card-wrapper" })
        resultNum = 1
        while len(results)>0:
            for i in range(len(results)):
                resDict = {}
                try:
                    # print("Title of Event:",results[i].find('div', attrs={'class': 'eds-is-hidden-accessible'}).text)
                    resDict["title"] = results[i].find('div', attrs={'class': 'eds-is-hidden-accessible'}).text
                except:
                    resDict["title"] = "NO DATA"
                try:
                    # print("Link of Event:",results[i].contents[0].select('a')[0]["href"])
                    resDict["link"] = results[i].contents[0].select('a')[0]["href"]
                except:
                    resDict["link"] = "NO DATA"
                try:
                    # print("Image of Event:",results[i].contents[0].select('img')[0]["src"])
                    resDict["image"] = results[i].contents[0].select('img')[0]["src"]
                except:
                    resDict["image"] = "NO DATA"
                try:
                    dateString = results[i].find("div",{ "class" : "eds-event-card-content__sub-title eds-text-color--ui-orange eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm" }).text
                    newDate =  validate(dateString)
                    print("Date and Time of Event:",  newDate )
                    resDict["date"] =  newDate
                except:
                    resDict["date"] = "NO DATA"
                try:
                    resDict["location"] = results[i].find("div",{ "data-subcontent-key" : "location" }).text
                except:
                    resDict["location"] = "NO DATA"
                events.append(resDict)
                # print(i)
                # print("-----------------",pageNum)
                resultNum+=1
            pageNum+=1
            url = 'https://www.eventbrite.com/d/{}--{}/{}/?page={}'.format(state,city,category,pageNum)
            response=requests.get(url,headers=headers)
            soup=BeautifulSoup(response.content,'html')
            results = soup.find_all("div",{ "class" : "search-event-card-wrapper" })
    API_KEY = '1Ms7iC-K52YCHkR70xuI_sXsZvQlHqhS3ze5DpUc_gnMm-D96G7O_GHKmu_COxuBckjlZCo7bAHkxSR1sDPMQ3lxH41VICcGlsUJPRUc1kmUrMJmROeSR4WgIQ04YnYx'
    ENDPOINT = 'https://api.yelp.com/v3/events'
    HEADERS = {'Authorization':'bearer %s' % API_KEY}
    if (category =="charity-and-causes--events"):
        for i in range(0,100,20):
            PARAMETERS = {'limit':20, 'categories':['charities'],'locale':'en_US','location':city,'offset':i,'start_date':utc_time}
            response = requests.get(url=ENDPOINT,params=PARAMETERS,headers=HEADERS)
            business_data = response.json()
            # print(business_data)
            for j in range(len(business_data["events"])):
                resDict = {}
                resDict["title"] = business_data["events"][j]["name"]
                resDict["link"] = business_data["events"][j]["tickets_url"]
                resDict["image"] = business_data["events"][j]["image_url"]
                resDict["date"] =  business_data["events"][j]["time_start"]
                resDict["location"] =business_data["events"][j]["location"]
                print("Date and Time of Event: yelp", business_data["events"][j]["time_start"])
                
                events.append(resDict)

    if(category=="lectures-books"):
    
        
        for i in range(0,100,20):
            PARAMETERS = {'limit':20, 'categories':['lectures-books'],'locale':'en_US','location':city,'offset':i,'start_date':utc_time}
            response = requests.get(url=ENDPOINT,params=PARAMETERS,headers=HEADERS)
            business_data = response.json()
            # print(business_data)
            for j in range(len(business_data["events"])):
                resDict = {}
                resDict["title"] = business_data["events"][j]["name"]
                resDict["link"] = business_data["events"][j]["tickets_url"]
                resDict["image"] = business_data["events"][j]["image_url"]
                resDict["date"] =  business_data["events"][j]["time_start"]
                print("Date and Time of Event: yelp", business_data["events"][j]["time_start"])
                resDict["location"] =business_data["events"][j]["location"]
                events.append(resDict)
    paginator = Paginator(events, 10)
    newevents = paginator.page(1)
    return newevents
    
 
def events_view(request):
    # initial user display

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            # event = form.save(commit=False)
            city = form['city'].value()
            state = form['state'].value()
            category = form['category'].value()
            # print(location)
            # print(category)
            events = returnResult(request,category, city,state)
            return render(request, "events/events.html", {"form": form, "events":events})
    form = EventForm()

    return render(request, "events/events.html", {"form": form})


