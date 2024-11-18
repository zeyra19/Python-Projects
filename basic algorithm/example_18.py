#özet: lambda ve filter'ı bir arada kullanarak ikiye bölünen sayıları bul
numbers = [2, 5, 8, 44]

sonuc = filter(lambda number: number % 2 == 0, numbers)
print(list(sonuc))
