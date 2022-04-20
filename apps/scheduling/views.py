from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.scheduling.models import Event
from django.http import HttpResponse
import ast
from django.views.generic import ListView
import datetime
from datetime import datetime
from .utils import Calendar
import json 
from datetime import date

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

def scheduleEvent(request):
    # add event to db
    # save event as a model
    data = dict(request.GET)
    print(data)
    print("---------------------")
    
    title = ast.literal_eval((data["event"][0]))["title"]
    location= ast.literal_eval((data["event"][0]))["location"]
    date =  datetime.strptime(ast.literal_eval((data["event"][0]))["date"], '%b %d %Y %I:%M %p')
    link = ast.literal_eval((data["event"][0]))["link"] 
    print(date)
    if (title == "NO DATA"):
        title = None
    if (location == "NO DATA"):
        location = None
    if (date == "NO DATA"):
        date = None
    if ( link == "NO DATA"):
        link = None
    # print(title)
    # print(location)
    # print(date)
    # print(link)

    print("------------------------------")
    new_entry = Event(event_name=title, event_location=location, event_date=date, event_link=link)
    new_entry.save()
    print("after it ")
    print(Event.objects.all())
    # event_name = models.CharField(max_length=500)
    # event_location =  models.CharField(max_length=500)
    # event_date =  models.DateTimeField()
    # event_link =  models.CharField(max_length=500)
    return render(request, "events/events.html")
def deleteEvent(request, event_id):
    #delete event
    print("inside delete_events")
    print(event_id)
    event= Event.objects.get(pk=event_id)
    url = event.event_link
    event.delete()

    events = list(Event.objects.all().values().order_by('event_date'))
    for i in events:
        # print("BEFORE")
        # print(i["event_date"])

        i['title']= i["event_name"]
        i['url']= i['event_link']
        i['start']= i["event_date"].isoformat()
        # print("AFTER")
        # print(i["start"])
        i['event_date'] = i['event_date'].strftime('%b %d %Y %I:%M %p')
        i['event_status'] = str(i['event_status']) 
        print(i['start'])
    print(events)
    dateTime = str(date.today())
     
    return render(request, "scheduling/scheduling.html",context={'events':events,'dateTime':dateTime,'eventRemoved':True,'eventUrlRemoved':url})

def registerEvent(request):
    print("INSIDE REGISTER EVENTS")
    data = dict(request.GET)
    event_id = int(data['event[eventid]'][0])
    event= Event.objects.get(pk=event_id)
    event.event_status = True
    event.save()
    print(event_id)
    events = list(Event.objects.all().values().order_by('event_date'))
    for i in events:
        # print("BEFORE")
        # print(i["event_date"])

        i['title']= i["event_name"]
        i['url']= i['event_link']
        i['start']= i["event_date"].isoformat()
        # print("AFTER")
        # print(i["start"])
        i['event_date'] = i['event_date'].strftime('%b %d %Y %I:%M %p')
        i['event_status'] = str(i['event_status']) 
        print(i['start'])
    print(events)
    dateTime = str(date.today())
    # print(dateTime)
    print(event.event_link)
    # return event.event_link
    return render(request, "scheduling/scheduling.html",context={'events':events,'dateTime':dateTime})
 

def startup(request):
    events = list(Event.objects.all().values().order_by('event_date'))
    for i in events:
        # print("BEFORE")
        # print(i["event_date"])

        i['title']= i["event_name"]
        i['url']= i['event_link']
        i['start']= i["event_date"].isoformat()
        # print("AFTER")
        # print(i["start"])
        i['event_date'] = i['event_date'].strftime('%b %d %Y %I:%M %p')
        i['event_status'] = str(i['event_status']) 
        print(i['start'])
    print(events)
    dateTime = str(date.today())
    # print(dateTime)

     
    return render(request, "scheduling/scheduling.html",context={'events':events,'dateTime':dateTime})