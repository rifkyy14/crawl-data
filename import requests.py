import requests
from bs4 import BeautifulSoup

url = "https://news.detik.com/indeks"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
urls = []
judul = []
gambar = []
tanggal_rilis = []
for elemen in soup.find_all('div', {'class': 'content'}):
   
   url_elemen = elemen.find('a')['href']
   urls.append(url_elemen)
    
   
   judul_elemen = elemen.find('h2').text
   judul.append(judul_elemen)
    
   
   gambar_elemen = elemen.find('img')['src']
   gambar.append(gambar_elemen)
    
    
   tanggal_rilis_elemen = elemen.find('span', {'class': 'date'}).text
   tanggal_rilis.append(tanggal_rilis_elemen)
   print("URL\t\tJudul\t\tGambar\t\tTanggal Rilis")
for i in range(len(urls)):
    print(f"{urls[i]}\t\t{judul[i]}\t\t{gambar[i]}\t\t{tanggal_rilis[i]}")