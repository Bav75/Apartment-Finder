#Import Modules 
import requests
import xml.dom.minidom
import xml.etree.ElementTree as ET

#API call parameters 
with open("zwsid.txt", "r") as id: #Read API key from locally stored file
    zwsid = id.read() #Set API key
address = "460+Davis+Court" 
citystatezip = "San+Francisco+California+94111"
rentzestimate = True

#Create response object
response = requests.post("http://www.zillow.com/webservice/GetDeepSearchResults.htm", 
    data = {"zws-id" : zwsid, "address" : address, "citystatezip" : citystatezip, "rentzestimate" : rentzestimate}
)

#Format response 
xml = ET.fromstring(response.content)


