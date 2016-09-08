from geopy.geocoders import Nominatim
import decimal
from factual import Factual
from factual.utils import circle
import json
from datetime import date
import calendar
import datetime


my_date = date.today()
my_day = calendar.day_name[my_date.weekday()]
my_day = my_day.lower()
factual = Factual('OAwHffzwwkan9LpstDBhOGOGmit7plcERqZpvE2J', 'gw28zCrtijknGrGDm9dVzC1v8HyFHi0HbEtGacL7', timeout=10.0)
s = factual.table('places').schema()
places = factual.table('places')
a = raw_input("Location A: ")
b = raw_input("Location B: ")
c = raw_input("What are you looking for: ")
#d = raw_input("Proximity from the midpoint (mtrs): ")
def findMidPlace(a, b, c, d):
	geolocator = Nominatim()
	locationA = geolocator.geocode(a)
	locationB = geolocator.geocode(b)
	midpointLat = (locationA.latitude + locationB.latitude)/2
	print midpointLat
	midpointLong = (locationA.longitude + locationB.longitude)/2
	print midpointLong
	strMidpointLat = str(midpointLat)
	strMidpointLong = str(midpointLong)
	midpointLocation = strMidpointLat + ", " + strMidpointLong
	newLocation = geolocator.reverse(midpointLocation)
	data = places.search(c).geo(circle(midpointLat, midpointLong, d)).limit(10).data()
	#cleanData = json.dumps([{'Name': x['name'], 'Address': x['address'], 'Tel': x['tel'], 'Timings':x['hours'][my_day][0][0]+' - ' + x['hours'][my_day][0][1]} for x in data],indent=2, sort_keys=True)
	cleanData = json.dumps([{'Name': x['name'], 'Address': x['address']} for x in data],indent=2, sort_keys=True)

	print cleanData
findMidPlace(a,b,c,500)
#Set the distance to 500
