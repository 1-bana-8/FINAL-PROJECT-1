import requests 
from bs4 import BeautifulSoup 
import csv 
a=["https://karki23.github.io/Weather-Data/Albury.html","https://karki23.github.io/Weather-Data/BadgerysCreek.html","https://karki23.github.io/Weather-Data/Cobar.html","https://karki23.github.io/Weather-Data/CoffsHarbour.html","https://karki23.github.io/Weather-Data/Moree.html","https://karki23.github.io/Weather-Data/Newcastle.html",
"https://karki23.github.io/Weather-Data/NorahHead.html","https://karki23.github.io/Weather-Data/NorfolkIsland.html","https://karki23.github.io/Weather-Data/Penrith.html","https://karki23.github.io/Weather-Data/Richmond.html","https://karki23.github.io/Weather-Data/Sydney.html","https://karki23.github.io/Weather-Data/SydneyAirport.html","https://karki23.github.io/Weather-Data/WaggaWagga.html","https://karki23.github.io/Weather-Data/Williamtown.html","https://karki23.github.io/Weather-Data/Wollongong.html","https://karki23.github.io/Weather-Data/Canberra.html","https://karki23.github.io/Weather-Data/Tuggeranong.html","https://karki23.github.io/Weather-Data/MountGinini.html",
"https://karki23.github.io/Weather-Data/Ballarat.html","https://karki23.github.io/Weather-Data/Bendigo.html","https://karki23.github.io/Weather-Data/Sale.html","https://karki23.github.io/Weather-Data/MelbourneAirport.html",
"https://karki23.github.io/Weather-Data/Melbourne.html","https://karki23.github.io/Weather-Data/Mildura.html","https://karki23.github.io/Weather-Data/Nhil.html","https://karki23.github.io/Weather-Data/Portland.html","https://karki23.github.io/Weather-Data/Watsonia.html","https://karki23.github.io/Weather-Data/Dartmoor.html","https://karki23.github.io/Weather-Data/Brisbane.html","https://karki23.github.io/Weather-Data/Cairns.html",
"https://karki23.github.io/Weather-Data/GoldCoast.html","https://karki23.github.io/Weather-Data/Townsville.html","https://karki23.github.io/Weather-Data/Adelaide.html","https://karki23.github.io/Weather-Data/MountGambier.html","https://karki23.github.io/Weather-Data/Nuriootpa.html","https://karki23.github.io/Weather-Data/Woomera.html","https://karki23.github.io/Weather-Data/Albany.html","https://karki23.github.io/Weather-Data/Witchcliffe.html","https://karki23.github.io/Weather-Data/PearceRAAF.html",
"https://karki23.github.io/Weather-Data/PerthAirport.html","https://karki23.github.io/Weather-Data/Perth.html","https://karki23.github.io/Weather-Data/SalmonGums.html","https://karki23.github.io/Weather-Data/Walpole.html","https://karki23.github.io/Weather-Data/Hobart.html","https://karki23.github.io/Weather-Data/Launceston.html","https://karki23.github.io/Weather-Data/AliceSprings.html",
"https://karki23.github.io/Weather-Data/Darwin.html","https://karki23.github.io/Weather-Data/Katherine.html","https://karki23.github.io/Weather-Data/Uluru.html"]

b=["Albury.csv","Badgerys Creek.csv","Cobar.csv","Coffs Harbour.csv","Moree.csv","Newcastle.csv","NorahHead.csv","Norfolk Island.csv","Penrith.csv",
"Richmond.csv","Sydney.csv","Sydney Airport.csv","Wagga Wagga.csv","William town.csv","Wollongong.csv","Canberra.csv","Tuggeranong.csv",
"Mount Ginini.csv","Ballarat.csv","Bendigo.csv","Sale.csv","Melbourne Airport.csv","Melbourne.csv","Mildura.csv","Nhil.csv","Portland.csv","Watsonia.csv",
"Dartmoor.csv","Brisbane.csv","Cairns.csv","Gold Coast.csv","Townsville.csv","Adelaide.csv","Mount Gambier.csv","Nuriootpa.csv","Woomera.csv",
"Albany.csv","Witchcliffe.csv","PearceRAAF.csv","Perth Airport.csv","Perth.csv","SalmonGums.csv","Walpole.csv","Hobart.csv","Launceston.csv","Alice Springs.csv","Darwin.csv","Katherine.csv","Uluru.csv"]


for l in range(0,len(a)):
    URL = a[l]
	x=requests.get(URL) 
	soup=BeautifulSoup(x.content, 'html5lib' )
	cfile=open(b[l],"w+",newline='')
	writer=csv.writer(cfile)
    for row in soup.find_all("tr"):
        csvrow=[]
        for cell in row.find_all(['td','th']):
            csvrow.append(cell.get_text())
            writer.writerow(csvrow)
    cfile.close()

	
    

	
	