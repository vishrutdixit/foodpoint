from geopy.geocoders import Nominatim
import decimal
from factual import Factual
from factual.utils import circle

factual = Factual('OAwHffzwwkan9LpstDBhOGOGmit7plcERqZpvE2J', 'gw28zCrtijknGrGDm9dVzC1v8HyFHi0HbEtGacL7')
s = factual.table('places').schema()
places = factual.table('places')




a = raw_input("Location A: ")
b = raw_input("Location B: ")
c = raw_input("What are you looking for: ")
d = raw_input("Proximity from the midpoint (ft): ")



def findMidpoint(a, b, c, d):
	geolocator = Nominatim()

	locationA = geolocator.geocode(a)

	locationB = geolocator.geocode(b)

	midpointLat = (locationA.latitude + locationB.latitude)/2
	midpointLong = (locationA.longitude + locationB.longitude)/2
	strMidpointLat = str(midpointLat)
	strMidpointLong = str(midpointLong)
	midpointLocation = strMidpointLat + ", " + strMidpointLong

	newLocation = geolocator.reverse(midpointLocation)
	print newLocation
	data = places.search(c).geo(circle(midpointLat, midpointLong, d)).limit(5).data()
	print(data)

findMidpoint(a,b,c,d)