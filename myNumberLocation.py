import  phonenumbers
import folium
from  myNumber import number
from phonenumbers import geocoder


key = "b8d3b35b7b784e39a505310e64a02ded"

samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber,"en")

print(yourLocation)


from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode


geocoder = OpenCageGeocode(key)

query = str(yourLocation)
resulte = geocoder.geocode(query)
let = resulte[0]['geometry']['lat']
lng = resulte[0]['geometry']['lng']
print(let,lng)

myMap= folium.Map(location=[let,lng], zoom_start = 9)
folium.Marker([let,lng],popup= yourLocation).add_to((myMap))

myMap.save('myLocation.html')