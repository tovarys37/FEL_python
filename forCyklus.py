#read file system!
# ------------------
import time
import os;
from urllib.request import urlopen


#f = open("DataInput.txt");
#e = f.readline();
#print(e[1:10],"\n -------")
#webData = f.read();
#print(webData[1:100])
#===========




response = urlopen('https://www.in-pocasi.cz/meteostanice/stanice.php?stanice=praha')
webDataS = response.read()

# ========  FIND DATA =========
webData = webDataS.decode("utf-8")
#print(webData)
teplota = "°C";
PoziceTeploty = webData.find(teplota)-4;

AktualniTeplota = webData[PoziceTeploty:PoziceTeploty+3];
CasMereni = webData[PoziceTeploty-26:PoziceTeploty-26+5];
#print('teplota / cas >',AktualniTeplota, CasMereni)



# ========  DATA SAVING =========
fileOutputName = "TemperatureOutput.txt";
if (os.path.isfile(fileOutputName)):
    file = open(fileOutputName, "a")
else:
    file = open(fileOutputName, "a")
    file.write('Čas, Teplota>')
    file.write("\n")

#print('teplota / cas >',AktualniTeplota, CasMereni)
file.write(CasMereni)
file.write(", ")
file.write(AktualniTeplota)
file.write("\n")
file.close()



# print('teplota / cas >',AktualniTeplota, CasMereni)



#=====
#file.read()
#file.readline(file)
#f.close()


#print(file.readline(file))
#read_data = f.read()
#DataInput.txt



