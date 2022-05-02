from django.shortcuts import render
from apps.scheduling.models import Event
import ast
import datetime
from datetime import datetime
import json 
from datetime import date



def scheduleEvent(request):
    '''function to add event to the db'''
    data = dict(request.GET)
    title = ast.literal_eval((data["event"][0]))["title"]
    location= ast.literal_eval((data["event"][0]))["location"]
    date =  datetime.strptime(ast.literal_eval((data["event"][0]))["date"], '%b %d %Y %I:%M %p')
    link = ast.literal_eval((data["event"][0]))["link"] 
    
    if (title == "NO DATA"):
        title = None
    if (location == "NO DATA"):
        location = None
    if (date == "NO DATA"):
        date = None
    if ( link == "NO DATA"):
        link = None
    
    try:
        #filter the event objects by user Id
        sessionUser = Event.objects.filter(user_id=request.user.id)
        #check if records for this user exists
        if(len(sessionUser)==0):
            #if it doesn't insert record
            new_entry = Event(user_id=request.user.id,event_name=title, event_location=location, event_date=date, event_link=link)
            new_entry.save()
        else:
            #if it does
            if (len(Event.objects.filter(user_id=request.user.id,event_link=link))==0):
                new_entry = Event(user_id=request.user.id,event_name=title, event_location=location, event_date=date, event_link=link)
                new_entry.save()
            else:
                return
                

    except:
        pass
    
    return render(request, "events/events.html")
def deleteEvent(request, event_id):
    '''function that deletes event from schedule'''
    #delete event
   
    event= Event.objects.get(pk=event_id)
    url = event.event_link
    event.delete()

    events = list(Event.objects.all().values().order_by('event_date'))
    for i in events:

        i['title']= i["event_name"]
        i['url']= i['event_link']
        i['start']= i["event_date"].isoformat()
        i['event_date'] = i['event_date'].strftime('%b %d %Y %I:%M %p')
        i['event_status'] = str(i['event_status']) 
        
    dateTime = str(date.today())
     
    return render(request, "scheduling/scheduling.html",context={'events':events,'dateTime':dateTime,'eventRemoved':True,'eventUrlRemoved':url})

def registerEvent(request):
    '''function to change registration status of event'''
    data = dict(request.GET)
    event_id = int(data['event[eventid]'][0])
    event= Event.objects.get(pk=event_id)
    event.event_status = True
    event.save()
    events = list(Event.objects.all().values().order_by('event_date'))
    for i in events:
        i['title']= i["event_name"]
        i['url']= i['event_link']
        i['start']= i["event_date"].isoformat()
        i['event_date'] = i['event_date'].strftime('%b %d %Y %I:%M %p')
        i['event_status'] = str(i['event_status']) 
    dateTime = str(date.today())
    return render(request, "scheduling/scheduling.html",context={'events':events,'dateTime':dateTime})
 

def startup(request):
    '''function to startup the scheduling system'''
    events = list(Event.objects.all().values().filter(user_id=request.user.id).order_by('event_date'))
    for i in events:
        i['title']= i["event_name"]
        i['url']= i['event_link']
        i['start']= i["event_date"].isoformat()
        i['event_date'] = i['event_date'].strftime('%b %d %Y %I:%M %p')
        i['event_status'] = str(i['event_status']) 
    
    dateTime = str(date.today())
     
    return render(request, "scheduling/scheduling.html",context={'events':events,'dateTime':dateTime})