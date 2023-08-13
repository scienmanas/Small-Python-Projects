import html
import requests
from bs4 import BeautifulSoup
unwanted_chars = ['\n', '\t', 'r', '\xa0', 'â\x80\x93'] # Edit this to include all characters you want to remove

def clean_up_text(text, unwanted_chars=unwanted_chars):
    
    for char in unwanted_chars:
        text = text.replace(char, '')

    return text

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

DataFromWebsite = requests.get(url=URL)

soup = BeautifulSoup(DataFromWebsite.text,"html.parser")
movie_titles = soup.find_all(name="h3", class_="title")

MoviesList = [clean_up_text(movie.getText()) for movie in movie_titles]
MoviesList = MoviesList[::-1]




try:
    with open(r"Python_Course\Day 45\Movies Scarapper\movies.txt", mode='a') as file:
        pass
except:
    with open(r"Python_Course\Day 45\Movies Scarapper\movies.txt", mode='w') as file:
        pass
finally:
    with open(r"Python_Course\Day 45\Movies Scarapper\movies.txt", mode='a') as file:
        for movie in MoviesList:
            file.write(f"{movie}\n")            

