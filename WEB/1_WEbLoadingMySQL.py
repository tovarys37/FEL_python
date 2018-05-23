
import os;
from lxml import html
import requests

page = requests.get('https://www.meteoskop.cz/pocasi/dejvice')
tree = html.fromstring(page.content)


#This will create a list of buyers:
now = tree.xpath('//div[@class="now"]/text()')
#This will create a list of prices
temp = tree.xpath('//div[@class="temp"]/text()')
#This will create a list of prices
date = tree.xpath('//span[@class="date"]/text()')

now = now[0].replace("dnes ","")
temp = temp[0].replace("°","")
date = date[0].replace("dnes (","")
date = date.replace(")","")

#print('Now: ', now)
#print('Time: ', temp)
#print('Date: ', date)


#fileHandle = open ( 'TemperatureOutput_dejvice.txt',"r" )
#lineList = fileHandle.readlines()
#fileHandle.close()
#print(lineList[-1])

#exit()

fileOutputName = "TemperatureOutput_dejvice.txt";
if (os.path.isfile(fileOutputName)):
    file = open(fileOutputName, "a")
else:
    file = open(fileOutputName, "a")
    file.write('Datum, Čas, Teplota>')
    file.write("\n")

#if f.read() = date


file.write(date)
file.write(", ")
file.write(now)
file.write(", ")
file.write(temp)
file.write("\n")
file.close()








