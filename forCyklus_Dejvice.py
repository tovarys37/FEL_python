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




response = urlopen('https://www.meteoskop.cz/pocasi/dejvice')
webDataS = response.read()

# ========  FIND DATA =========
webData = webDataS.decode("utf-8")
print(webData)
teplota = "/static/img/states/60x60-white/";
PoziceTeploty = webData.find(teplota);
print(PoziceTeploty)
PoziceTeploty = 4117;

AktualniTeplota = webData[PoziceTeploty-50:PoziceTeploty-48];
CasMereni = webData[PoziceTeploty+168:PoziceTeploty+173];
print('teplota / cas >',AktualniTeplota, CasMereni)

exit


# ========  DATA SAVING =========
fileOutputName = "TemperatureOutput_dejvice.txt";
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



