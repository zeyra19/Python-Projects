#özet: api dan veri çek ve bunu fonskiyonlarla özelleştir
import requests


class MovieDb:
    def __init__(self):


    def get_populars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def get_related(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()


movieApi = MovieDb()

while True:
    secim = input("1-Show Result\n2-Search Movie\n3-Exit\n...:")

    if secim == "3":
        break
    else:
        if secim == "1":
            movies = movieApi.get_populars()
            for movie in movies['results']:
                print(movie['title'], "bu filmin puanı:", movie['vote_average'])

        if secim == "2":
            keyword = input("Search for your movie by entering words: ")
            movies = movieApi.get_related(keyword)
            for movie in movies['results']:
                # hem namei hem idyi alacağım.
                print(movie['name'], movie['id'])
