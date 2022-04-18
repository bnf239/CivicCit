from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.scheduling.models import Event
import ast
from django.views.generic import ListView
import datetime
from datetime import datetime
from .utils import Calendar
import json 
from datetime import date
def scheduleEvent(request):
    # add event to db
    # save event as a model
    data = dict(request.GET)
    print(data)
    print("---------------------")
    print("title", ast.literal_eval((data["event"][0]))["title"])
    print("location",ast.literal_eval((data["event"][0]))["location"])
    print("date",ast.literal_eval((data["event"][0]))["date"] )
    print("link",ast.literal_eval((data["event"][0]))["link"] )
    print("------------------------------")
    new_entry = Event(event_name=ast.literal_eval((data["event"][0]))["title"], event_location=ast.literal_eval((data["event"][0]))["location"], event_date=ast.literal_eval((data["event"][0]))["date"], event_link=ast.literal_eval((data["event"][0]))["link"])
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
    event.delete()

    events = list(Event.objects.all().values() )
    for i in events:
        i['title']= i["event_name"]
        i['url']= i['event_link']
        i['start']= i["event_date"].isoformat()
        i['event_date'] = i['event_date'].strftime('%b %d %Y %I:%M %p')
    print(events)
     
    return render(request, "scheduling/scheduling.html",context={'events':events})



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
        print(i['start'])
   # print(events)
    dateTime = str(date.today())
    # print(dateTime)

     
    return render(request, "scheduling/scheduling.html",context={'events':events,'dateTime':dateTime})