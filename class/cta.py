
# Periodically monitor the bus system and see whether an identified
# bus returns to within a half-mile of Dave's office
# http://ctabustracker.com/bustime/home.jsp
# Bus Tracker APIs
# https://www.transitchicago.com/developers/bustracker/

from selenium import webdriver
import time
import urllib.request
from xml.etree.ElementTree import parse
import time
from xml.etree import ElementTree

# Latitude of Dave's office.
office_lat = 41.980262

# Set of bus ids that you want to monitor.  Change to match
# the output of the find_north.py script
busids = {'4377'}


def distance(lat1, lat2):
    'Return approx miles between lat1 and lat2'
    return 69 * abs(lat1 - lat2)


#driver = webdriver.Firefox()

while True:
    u = urllib.request.urlopen(
        'https://www.ctabustracker.com/bustime/api/v2/getvehicles?key=YOURKEY&vid=4377')
    print("Running")
    
    print(u.read())
    doc = parse(u)
    #xmlstr = ElementTree.tostring(doc, encoding='utf8', method='xml')
    #print(xmlstr)
    print(type(doc))

    for bus in doc.findall('vehicle'):
        busid = bus.findtext('vid')
        if busid in busids:
            lat = float(bus.findtext('lat'))
            lon = float(bus.findtext('lon'))
            dist = distance(lat, office_lat)
            print('%s Latitude: %0.2f Longitude: %02.f Distance %0.2f miles' % (busid, lat, lon, dist))

            # if dist < 1.3:
            # Launch a browser to see on a map
            x = 'www.openstreetmap.org/?mlat=%f&mlon=%f&zoom=14' % (lat, lon)
            refreshrate = 3
            #driver.get("http://" + x)
            time.sleep(refreshrate)
            #driver.refresh()
