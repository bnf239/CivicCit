from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



def scheduleEvent(request):
    # add event to db
    # save event as a model
    print(request)
    print("in here schedule")
    print(request.GET)
    print("after it ")
    return render(request, "events/events.html")
    
def startup(request):
    return render(request, "scheduling/scheduling.html")