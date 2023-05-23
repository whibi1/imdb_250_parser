import requests
from bs4 import BeautifulSoup
URL="https://www.imdb.com/chart/top/"
response=requests.get(URL)
soup=BeautifulSoup(response.text,"html.parser")

basliklar= soup.find_all("td",{"class":"titleColumn"})
ratingler=soup.find_all("td",{"class":"ratingColumn imdbRating"})
a=float(input("Lütfen Rating puanı giriniz:"))
for baslik,rating in zip (basliklar,ratingler):
    baslik=baslik.text
    baslik=baslik.strip()
    baslik=baslik.replace("\n","")
    rating=rating.text
    rating=rating.strip()
    rating=rating.replace("\n","")

    if (float(rating) >a ):
        print("Film İsmi: {} Filmin Ratingi: {}".format(baslik,rating))