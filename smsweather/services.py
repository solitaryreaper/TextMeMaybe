from twilio.rest import TwilioRestClient
import twilio
import forecastio
from pygeocoder import Geocoder
 
# Your Account Sid and Auth Token from twilio.com/user/account
TWILIO_ACCOUNT_SID = "ACc5e06276e9acc6426aab3b0e57dc8809"
TWILIO_AUTH_TOKEN  = "6ad472db3444e0f15c4770f8c8b56f83"
twilio_client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Trail twilio number
MY_TWILIO_NUMBER = "+19797733224"
USER_MOBILE_NUMBER = "+15122010228"

# API key for forecast.io
FORECAST_KEY = "a2f3dde76857f35e811c6372fcc367ab"

def send_twilio_message(message, to_num, from_num):
    """
        Sends a message to a subscriber's phone number using Twilio API
    """
    print "Sending quote " + message + " to " + to_num + " from " + from_num
    try:
        twilio_client.sms.messages.create(body=message, to=to_num, from_=from_num)
    except twilio.TwilioRestException as e:
        print e
    
def get_weather_by_coordinates(latitude, longitude):
    """
        Returns the current weather for the specified co-ordinates
    """
    forecast = forecastio.load_forecast(FORECAST_KEY, latitude, longitude)
    by_hour = forecast.hourly()
    
    return str(forecast.hourly().data[0].temperature) + " F , " + by_hour.summary
  
def get_coordinates_from_location(location):
    """
        Returns the co-ordinates from the location
    """        
    results = Geocoder.geocode(location)
    return str(results[0].coordinates)
    
def get_weather_by_location(location):
    """
        Returns the local weather for a location and sends a message on the registered number
    """  
    coordinates = get_coordinates_from_location(location)
    tokens = coordinates.split(",")
    latitude = float(tokens[0].replace("(","").strip())
    longitude = float(tokens[1].replace(")","").strip())
    print "Found co-ordinates. Latitude : " + str(latitude) + ", Longitude : " + str(longitude)
    
    weather = location + " Weather : " + get_weather_by_coordinates(latitude, longitude)
    print "Found weather : " + weather
    return weather
      
if __name__ == '__main__':
    location = "Austin"
    weather = get_weather_by_location(location)
    
    send_twilio_message(weather, USER_MOBILE_NUMBER, MY_TWILIO_NUMBER)
    print "Sent message to user with weather updates for " + location