from geopy.geocoders import Nominatim
import decimal
from factual import Factual
from factual.utils import circle
import json

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
	midpointLong = (locationA.longitude + locationB.longitude)/2
	strMidpointLat = str(midpointLat)
	strMidpointLong = str(midpointLong)
	midpointLocation = strMidpointLat + ", " + strMidpointLong

	newLocation = geolocator.reverse(midpointLocation)
	#print newLocation
	data = places.search(c).geo(circle(midpointLat, midpointLong, d)).limit(10).data()
	clean = json.dumps([{'name': x['name'], 'address': x['address'], 'tel': x['tel']} for x in data],indent=2, sort_keys=True)
	print clean
findMidPlace(a,b,c,500)
