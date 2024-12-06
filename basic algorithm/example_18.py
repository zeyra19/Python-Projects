# #özet: lambda ve filter'ı bir arada kullanarak ikiye bölünen sayıları bul
numbers = [2, 5, 8, 44]

sonuc = filter(lambda number: number % 2 == 0, numbers)
print(list(sonuc))


#özet: while ile döngü oluştur
i = 0
while i <= 12:
    i += 1
    print("kendimi tekrar ediyorum")


#özet: liste içinde mi bak
günler = ["pazartesi", "salı", "çarşamba"]

print("cuma" in günler) #FALSE
print("pazartesi" in günler) #TRUE

#özet: belirli fiyattaki kitapları getir
kitaplar = [
    {'yazar': 'Orhan Pamuk', 'kitap': 'Kar', 'fiyat': 35},
    {'yazar': 'Franz Kafka', 'kitap': 'Dava', 'fiyat': 25},
    {'yazar': 'George Orwell', 'kitap': '1984', 'fiyat': 30},
    {'yazar': 'J.R.R. Tolkien', 'kitap': 'Yüzüklerin Efendisi', 'fiyat': 50}
]

#özet: o fiyattaki kitapları getirecek
fiyat_gir = int(input("Hangi fiyatta kitap arıyorsunuz"))

for kitap in kitaplar:
    if kitap["fiyat"] == fiyat_gir:
        print("işte aadığın kitap", kitap)


#özet: fiyata yakın olan kitapları getirecek
butce = int(input("Bütçeniz ne kadar"))

for kitap in kitaplar:
    if kitap["fiyat"] <= butce:
        print("işte aradığınız kitaplar", kitap)