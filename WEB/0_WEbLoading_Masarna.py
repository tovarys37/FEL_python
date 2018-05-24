import os;
import lxml
from lxml import html
import requests
import time

from time import gmtime, strftime
import http.client, urllib.request, urllib.parse, urllib.error
key = 'FL3RBFOY4H3YCAE1' # Thingspeak channel to update


#def _WEbLoading_Strahov2(a, b):



#Report Raspberry Pi internal temperature to Thingspeak Channel
def thermometer(tempT):
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        #temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        casT = time.time();
        params = urllib.parse.urlencode({'field1': tempT, 'field2':casT, 'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            #print(temp)
            #print(response.status, response.reason)
            data = response.read()
            conn.close()
            print("connection OK")
        except:
            print("connection failed")
        break









ii=0
while (ii < 500):
    ii = ii + 1
    #print("Ulozeni c. " + str(ii))
    page = requests.get('http://teplomer.mk.cvut.cz/')
    tree = html.fromstring(page.content)
    data = tree.xpath('//div[@class="teplota1 "]/text()')
    temp = data[0]
    temp = temp.replace("\n\t\t", "")
    temp = temp.replace("\xa0°C\n\t", "")
    tempT = temp.replace(",", ".")
    print(float(tempT))
    thermometer(float(tempT))
    # print(+' {:.3f} \n'.format(gettemp(id2)/float(1000)))
    #print('online ulozeni zanama')
    time.sleep(60*4.5/2)
print("Good bye!")




