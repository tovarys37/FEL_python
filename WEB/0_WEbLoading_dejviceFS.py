

import os;
from lxml import html
import requests
import time



#def 0_WEbLoading_dejviceFS2(a, b):

page = requests.get('http://tzb.fsv.cvut.cz/projects/climadata/wx.html')
tree = html.fromstring(page.content)


#This will create a list of buyers:
#now = tree.xpath('//div[@class="now"]/text()')
#This will create a list of prices
#temp = tree.xpath('//div[@class="temp"]/text()')
#This will create a list of prices
#date = tree.xpath('//span[@class="date"]/text()')


data = tree.xpath('//div[@class="leftSideBar"]//ul//li/text()')
temp = data[0]
temp = temp.replace("Nyní: ", "")


date = time.strftime("%d.%m.%Y")
ttime = time.strftime("%H:%M")

print('Datum: ', date)
print('cas: ', ttime)
print('Temp: ', temp)



#fileHandle = open ( 'TemperatureOutput_dejvice.txt',"r" )
#lineList = fileHandle.readlines()
#fileHandle.close()
#print(lineList[-1])


fileOutputName = "TempOut_Dejvice_FS.txt";
if (os.path.isfile(fileOutputName)):
    file = open(fileOutputName, "a")
else:
    file = open(fileOutputName, "a")
    file.write('== Dejvice, FS ===>')
    file.write("\n")
    file.write('== Datum == Čas == Teplota ==')
    file.write("\n")


file.write(date)
file.write(", ")
file.write(ttime)
file.write(", ")
file.write(temp)
file.write("\n")
file.close()








