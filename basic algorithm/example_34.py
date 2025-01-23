# import requests
#
# data = "Data "
#
# input_data = input("......")
# print(f"{data}: {input_data}")
#
# yeni_data = "ve birleşen data"
# birlesmis_data = data + yeni_data
# print(birlesmis_data)
#
# tarih = "2025-01--23"
# url = f"urlexampleurlexample/date={tarih}"
#
# response = requests.get(url)
# if response.status_code == 200:
#     print(response.json())
# else:
#     print(f"istek başarısız oldu: status code {response.status_code}")


harfler = ["a", "b", "c", "d", "e"]


for harf, char in enumerate(harfler, start=1):
    print(f"{harf}-{char}")
