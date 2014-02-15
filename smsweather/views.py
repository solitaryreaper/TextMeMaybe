from django.http import HttpResponse
from smsweather.services import get_weather_by_location
import twilio.twiml
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello, world. Welcome to the weather texting app ..")

def getweather(request, location):
    """
        Returns the weather for the requested location
    """
    weather = get_weather_by_location(location)
    resp = twilio.twiml.Response()   
    resp.sms(weather)
    print "Twilio's response for " + location + "'s weather : " + str(resp)      
    return HttpResponse(str(resp))

@csrf_exempt
def postweather(request):
    """
        Intercepts a POST request from twilio server, fetches the message parameters and
        then returns the weather for the specified city in TwiML format.
    """
    params = request.POST
    print "POST request parameters : " + str(params)

    location = params['Body'].strip()
    
    weather = get_weather_by_location(location)
    resp = twilio.twiml.Response()   
    resp.sms(weather)
    print "Twilio's response for " + location + "'s weather : " + str(resp)      
    return HttpResponse(str(resp))

    



