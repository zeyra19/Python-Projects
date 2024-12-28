# özet: use book api
import requests

url = "https://www.googleapis.com/books/v1/volumes?q=api"
response = requests.get(url)
data = response.json()

# özet: datanın içindeki itemsları gez, öyle bir şey yoksa boş listeye ata
for book in data.get("items", []):
    # "title" anahtarı kesinlikle mevcut olmalıdır. Aksi halde bir KeyError hatası alırsın.
    print(book['volumeInfo']['title'])
    # authors Anahtarının Opsiyonel Olması onu get ile çekebileceğim anlamına gelir. direkt çekersem keyerror hatası verir
    # Bu hatayı önlemek için .get("authors") kullanılır
    print(book['volumeInfo'].get('authors'))
