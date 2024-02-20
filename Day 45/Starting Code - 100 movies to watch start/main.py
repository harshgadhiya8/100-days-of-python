import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
empire_webpage = response.text
movies_to_watch  = []
soup = BeautifulSoup(empire_webpage,'html.parser')
movie = soup.select("article-title-description article-title-description__text h3")
movies = soup.find_all(name = 'h3',class_="title")
for movie in movies:
    movies_to_watch.append(movie.getText())
movies_to_watch.reverse()

with open('movies.txt',mode='a',encoding='utf-8') as file:
    for movie in movies_to_watch:
        file.write(movie+"\n")
