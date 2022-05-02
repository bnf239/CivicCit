#imports necessary for Events Functionality
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .forms import EventForm
import re
import calendar
import datetime
from datetime import datetime

def validate(dateString):
    '''function will take dateString and return an appropriate format'''
    if(len(dateString)==0):
        return "NO DATA"
    else:
        dateString = dateString.split(',')
        date = dateString[1].strip()+' 2022'
        time = (re.findall(r".*(?:PM|AM)", dateString[2].strip()))[0]
        newDate = date + '  ' + time
        dtobject = datetime.strptime(newDate, '%b %d %Y %I:%M %p')
        return str(dtobject.strftime('%b %d %Y %I:%M %p'))

def getResults(category, city,state,pageNum):
    '''function returns the search results given 
    pagenumber and parameters'''

    city =city.lower()
    state = state.lower()
    events = []
     
    date = datetime.utcnow()
    utc_time = calendar.timegm(date.utctimetuple())
    
    if (category != "lectures-books"):
        
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
        url = 'https://www.eventbrite.com/d/{}--{}/{}/?page={}'.format(state,city,category,pageNum)
       
        response=requests.get(url,headers,verify=False)

        soup=BeautifulSoup(response.content,'html')

        results = soup.find_all("div",{ "class" : "search-event-card-wrapper" })
        ''' web scraping through html content for data requested'''
        if (len(results)>0):
            for i in range(len(results)):
                resDict = {}
                try:
                    resDict["title"] = results[i].find('div', attrs={'class': 'eds-is-hidden-accessible'}).text
                except:
                    resDict["title"] = "NO DATA"
                try:
                    resDict["link"] = results[i].contents[0].select('a')[0]["href"]
                except:
                    resDict["link"] = "NO DATA"
                try:
                    resDict["image"] = results[i].contents[0].select('img')[0]["data-src"]
                except:
                    try:
                        resDict["image"] = results[i].contents[0].select('img')[0]["src"]
                    except:
                        resDict["image"] = "NO DATA"

                try:
                    dateString = results[i].find("div",{ "class" : "eds-event-card-content__sub-title" }).text
                    newDate =  validate(dateString)
                    resDict["date"] =  newDate
                except:
                    resDict["date"] = "NO DATA"
                try:
                    resDict["location"] = results[i].find("div",{ "data-subcontent-key" : "location" }).text
                except:
                    resDict["location"] = "NO DATA"
                
                if (resDict["title"]!= "NO DATA" and resDict["link"] != "NO DATA" and  resDict["location"] != "NO DATA" and resDict["date"] != "NO DATA"):
                    events.append(resDict)
        else:
            #no more results
            pass
    
    
    elif(category=="lectures-books"):
        '''yelp api'''
        API_KEY = '1Ms7iC-K52YCHkR70xuI_sXsZvQlHqhS3ze5DpUc_gnMm-D96G7O_GHKmu_COxuBckjlZCo7bAHkxSR1sDPMQ3lxH41VICcGlsUJPRUc1kmUrMJmROeSR4WgIQ04YnYx'
        ENDPOINT = 'https://api.yelp.com/v3/events'
        HEADERS = {'Authorization':'bearer %s' % API_KEY}
        startingIndex = (pageNum-1)*20
        
        PARAMETERS = {'limit':20, 'categories':['lectures-books'],'locale':'en_US','location':city,'offset':startingIndex,'start_date':utc_time}
        response = requests.get(url=ENDPOINT,params=PARAMETERS,headers=HEADERS)
        business_data = response.json()
       
        for j in range(len(business_data["events"])):
            resDict = {}
            resDict["title"] = business_data["events"][j]["name"]
            resDict["link"] = business_data["events"][j]["tickets_url"]
            resDict["image"] = business_data["events"][j]["image_url"]
            resDict["date"] =  str((datetime.fromisoformat(business_data["events"][j]["time_start"])).strftime('%b %d %Y %I:%M %p'))
            resDict["location"] = ' '.join(business_data["events"][j]["location"]['display_address'])
            events.append(resDict)
        
    return events




def checkNextResult(category, city,state,pageNum):

    '''
    function returns true or false depending on 
    whether there are more search results
    '''
    
    if(pageNum<=0):
        return False

    city =city.lower()
    state = state.lower()

    if (category=="lectures-books"):
        date = datetime.utcnow()
        utc_time = calendar.timegm(date.utctimetuple())
        
        API_KEY = '1Ms7iC-K52YCHkR70xuI_sXsZvQlHqhS3ze5DpUc_gnMm-D96G7O_GHKmu_COxuBckjlZCo7bAHkxSR1sDPMQ3lxH41VICcGlsUJPRUc1kmUrMJmROeSR4WgIQ04YnYx'
        ENDPOINT = 'https://api.yelp.com/v3/events'
        HEADERS = {'Authorization':'bearer %s' % API_KEY}
        startingIndex = (pageNum-1)*20
       
        PARAMETERS = {'limit':20, 'categories':['lectures-books'],'locale':'en_US','location':city,'offset':startingIndex,'start_date':utc_time}
        response = requests.get(url=ENDPOINT,params=PARAMETERS,headers=HEADERS)
        if(len(response.json()["events"])==0):
            return False
        else:
            return True

    else:
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
        url = 'https://www.eventbrite.com/d/{}--{}/{}/?page={}'.format(state,city,category,pageNum)

        response=requests.get(url,headers)

        soup=BeautifulSoup(response.content,'html')

        results = soup.find_all("div",{ "class" : "search-event-card-wrapper" })
        
        if(len(results)>0):
            return True
        else:
            return False


    
 
def events_view(request):
    # initial user display
    # intialize the page number
    pageNum=0
    if request.method == "POST":
        #check the type of button pressed
        if(request.POST['type']=="search"):
            pageNum = 1
        elif(request.POST['type']=="next"):
            pageNum = int(request.POST['num']) + 1
        elif(request.POST['type']=="prev" and int(request.POST['num'])>1):
            pageNum = int(request.POST['num']) - 1
        
        form = EventForm(request.POST)
        
        if form.is_valid():
            emptyList = False

            #retrieve input values
            city = form['city'].value()
            state = form['state'].value()
            category = form['category'].value()
           
            #get results
            events = getResults(category, city,state,pageNum)

            #check if next and previous pages exists
            nextButton = checkNextResult(category, city,state,pageNum+1)
            previousButton= checkNextResult(category, city,state,pageNum-1)
          
          
            num = pageNum
            if (len(events)==0):
                emptyList = True
           
            
            return render(request, "events/events.html", {"form": form, "events":events,"num":num,"nextButton":nextButton,"previousButton":previousButton,"emptyList":emptyList})
    form = EventForm()
    return render(request, "events/events.html", {"form": form,})


