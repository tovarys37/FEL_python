
import os;
from lxml import html
import requests
import time



#def _WEbLoading_Strahov2(a, b):


page = requests.get('https://www.in-pocasi.cz/meteostanice/stanice.php?stanice=praha')
tree = html.fromstring(page.content)


#This will create a list of buyers:
#now = tree.xpath('//table[@class="oblastits"//tbody]/text()')
#This will create a list of prices
#temp = tree.xpath('//div[@class="temp"]/text()')
#This will create a list of prices
#date = tree.xpath('//span[@class="date"]/text()')

data = tree.xpath('//table//b/text()')

ttime = data[6]
temp = data[7]
date = time.strftime("%d.%m.%Y")

#now = now[0].replace("dnes ","")
#temp = temp[0].replace("°","")
#date = date[0].replace("dnes (","")
#date = date.replace(")","")

print('Now: ', ttime)
print('Time: ', temp)
print('Date: ', date)


# Pridavani jen kdyz je potreba
#fileHandle = open ( 'asdasd.txt',"r" )
#lineList = fileHandle.readlines()
#fileHandle.close()
#print(lineList[-1])


fileOutputName = "TempOut_Strahov_inPocasi.txt";
if (os.path.isfile(fileOutputName)):
    file = open(fileOutputName, "a")
else:
    file = open(fileOutputName, "a")
    file.write('== Strahov, inPocasi ===>')
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








