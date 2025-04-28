from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city='indore'    
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=afc38ce51c1fe0553670d4a24a2337da'
    PARAMS={'units':'metric'}

    # Google Custom Search API credentials
    API_Key='AIzaSyDM4cxeK70u60BYY62EqRs0h8d9uoV0AIw'
    SEARCH_ENGINE_ID='860656cc4641c4f22'
    query=city +"1920*1080"
    page=1
    start=(page-1)*10+1
    searchType='image'
    city_url= f"https://www.googleapis.com/customsearch/v1?q={query}&cx={SEARCH_ENGINE_ID}&key={API_Key}&searchType={searchType}&num=10&start={start}"
    data=requests.get(city_url).json()
    count=1
    search_items=data.get('items')
    image_url =search_items[0]['link'] if search_items else None
    
    
    try:
        data=requests.get(url,PARAMS).json()
        description=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        temp=data['main']['temp']

        day=datetime.date.today()

        return render(request,'weatherapp/index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city,'exception_occurred':False,'image_url':image_url} )
    except:
        exception_occurred = True
        messages.error(request, 'City not found')
        return render(request,'weatherapp/index.html',{'description':'clear sky','icon':'01d','temp':'25','city':'indor', 'exception_occurred':exception_occurred})