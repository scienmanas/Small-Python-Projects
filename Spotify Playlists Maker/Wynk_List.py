import requests
from bs4 import BeautifulSoup

URL = "https://wynk.in/music/playlist/100-greatest-romantic-hits-bollywood/bb_1522659831847"

DataFromWebsite = requests.get(url=URL)

soup = BeautifulSoup(DataFromWebsite.text,"html.parser")

Songs = soup.find_all(name="a")
SongsList = [song.getText() for song in Songs]
print(SongsList)

# Won't work just a try can't scap the data of website