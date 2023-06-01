url = "https://www.backmarket.fr/fr-fr/p/iphone-13-pro-128-go-vert-alpin-debloque-tout-operateur/35d85a1e-6fa2-4331-ad51-a6e4c2a61a9e#l=10"
url2="https://www.backmarket.fr/fr-fr/p/iphone-13-pro-128-go-bleu-alpin-debloque-tout-operateur/f597a490-5e4c-450c-88a8-14be4d46f9c1#l=10"
# import HTMLSession from requests_html
from requests_html import HTMLSession
from bs4 import BeautifulSoup
# create an HTML Session object
session = HTMLSession()
 
# Use the object above to connect to needed webpage
resp = session.get(url)
 
print(resp.status_code)
# Run JavaScript code on webpage

#resp.html.render()
string2=resp.html.html
soup = BeautifulSoup(string2, 'html.parser')


price_nodes = soup.find_all('div', class_='w-full')


price=price_nodes[14].text.strip()
result=price[-8:]
print(result[:-2])


session = HTMLSession()
 
# Use the object above to connect to needed webpage
resp = session.get(url2)
 
print(resp.status_code)


string2=resp.html.html
soup = BeautifulSoup(string2, 'html.parser')


price_nodes = soup.find_all('div', class_='w-full')


price=price_nodes[14].text.strip()
result2=price[-8:]
print(result2[:-2])







from datetime import datetime

now = datetime.now()
date_time = now.strftime("%d/%m/%Y %H:%M")

print("Date et heure actuelles : ", date_time)


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("data.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("Data_backmarket") #open sheet
sheet = sheet.sheet1 #replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1
def add_row(sheet,date:str,prix:str,prix2:str):
    all_cells = sheet.range('A1:B2000')
    n_row=0
    for e in all_cells:
        f=e.value
        if(f!="") :
            n_row+=1
    newRow=int(n_row/2) +1
    sRow='A'+str(newRow)
    print(sRow)
    sheet.update(sRow,[[date,prix,prix2]])
print(result[:-2].strip())
add_row(sheet,date_time,result[:-2].strip(),result2[:-2].strip())