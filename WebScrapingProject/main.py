import requests
from bs4 import BeautifulSoup


URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")

all_movies = soup.findAll("strong")
movie_list = [movie.getText() for movie in all_movies]

new_movies = [movie for movie in movie_list if movie != "Director:" and movie != "Starring:" and movie != "READ MORE:" and movie != "Directors:"]
movies = new_movies[::-1]

try:
    with open("Top100Movies.txt", "x") as file:
        for movie in movies:
            file.write(f"{movie}\n")
        print("Movies list created!")
except FileExistsError:
    print("File exists in drectory!")




