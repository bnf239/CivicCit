from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.scheduling.models import Event
import ast

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
    
def startup(request):
    events = Event.objects.all().values() 
     
    return render(request, "scheduling/scheduling.html",context={'events':events})