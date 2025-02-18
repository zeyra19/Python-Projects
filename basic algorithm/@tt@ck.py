import requests
import threading

url = "example.com"

num_request = 5

def send_request():
    try:
        response = requests.get(url)
        print(response.status_code)
    except requests.exceptions.RequestException as e:
        print("error", e)

threads = []

for _ in range(num_request):
    t = threading.Thread(target=send_request)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("complete")