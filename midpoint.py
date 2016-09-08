from geopy.geocoders import Nominatim
import decimal
from factual import Factual
from factual.utils import circle
import json
from datetime import date
import calendar
import datetime
from twilio.rest import TwilioRestClient
account = "AC066cf83ba54417d23c093aa52385e596"
token = "7249ccefafe3e3e1c1e9b9319d3a7b9c"
client = TwilioRestClient(account, token)
factualAccount = "OAwHffzwwkan9LpstDBhOGOGmit7plcERqZpvE2J"
factualAuth = "gw28zCrtijknGrGDm9dVzC1v8HyFHi0HbEtGacL7"
factual = Factual(factualAccount, factualAuth, timeout=20.0)

#Globals
locations = []
latitude = []
longitude = []


#Used for checking timings on the day. Feature coming soon
my_date = date.today()
my_day = calendar.day_name[my_date.weekday()]
my_day = my_day.lower()


#Factual setup
s = factual.table('places').schema()
places = factual.table('places')


peopleNumber = raw_input("How many people are you going out with: ")
#raw input in string type
peopleNumber = int(peopleNumber)
#cast string to int



def promptLocation(peopleNumber):
	for number in range(peopleNumber):
		locations.append(raw_input("Insert location " + str((number + 1)) + " : "))

def convertToLatLong(locations):
	geolocator = Nominatim()
	for location in locations:
		locationCoordinates = geolocator.geocode(location, timeout=None)
		latitude.append(locationCoordinates.latitude)
		longitude.append(locationCoordinates.longitude)

def findMidPlace(latitude, longitude):
	geolocator = Nominatim()
	latitudeSum = sum(latitude)
	longitudeSum = sum(longitude)
	latitudeAverage = latitudeSum / len(latitude)
	longitudeAverage = longitudeSum / len(longitude)
	strlatitudeAverage = str(latitudeAverage)
	strlongitudeAverage = str(longitudeAverage)
	midpointLocation = strlatitudeAverage + ", " + strlongitudeAverage
	newLocation = geolocator.reverse(midpointLocation)
	data = places.search(c).geo(circle(latitudeAverage, longitudeAverage, 1000)).limit(10).data()
	resultingData = json.dumps([{'Name': x['name'], 'Address': x['address'], 'Telephone': x['tel']} for x in data],indent=2, sort_keys=True)
	print resultingData


	indexValue = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
	if (peopleNumber == 1):
		message = client.messages.create(to="+12244029741", from_="+12244073037", body= "These are the places around you" + ": " + resultingData)
	elif (peopleNumber <= 10 and peopleNumber > 1):
		a = indexValue[peopleNumber]
		message = client.messages.create(to="+12244029741", from_="+12244073037", body= "These are the places that are between you " + a + ": " + '\n' + resultingData)
	else:
		message = client.messages.create(to="+12244029741", from_="+12244073037", body= "These are the places that are between your group " + a + ": " + '\n' + resultingData)



#Main Activity	
if(peopleNumber == 0):
	print("Sorry, Try Again")
else:
	promptLocation(peopleNumber)
	type(peopleNumber)
	c = raw_input("What are you looking for: ")
	convertToLatLong(locations)
	findMidPlace(latitude, longitude)








