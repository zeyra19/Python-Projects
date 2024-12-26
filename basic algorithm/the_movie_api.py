import requests


class MovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "2716b69a59baef16c9bfa5750a9cdfac"

    def get_populars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()


movieApi = MovieDb()

while True:
    secim = input("1-Show Result\n2-Exit\n...:")

    if secim == "2":
        break
    else:
        if secim == "1":
            movies = movieApi.get_populars()
            for movie in movies['results']:
                print(movie['title'])
        break