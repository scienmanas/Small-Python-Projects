import requests
from bs4 import BeautifulSoup

user_input = input("Which year you want to travel to? Enter in YYYY-MM-DD format: ")
URL = "https://www.billboard.com/charts/hot-100/" + user_input
DataFromWebsite = requests.get(url=URL)

soup = BeautifulSoup(DataFromWebsite.text,"html.parser")

Songs = soup.select("li ul li h3")
SongsList = [song.getText().strip() for song in Songs]