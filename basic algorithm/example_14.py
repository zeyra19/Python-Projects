#özet: Bir firmanın, yılın ilk 6 ayındaki buzdolabı satış fiyatları buzdolabı isimli dizide tutulmaktadır.
# 400 adetten fazla buzdolabı satılan aylar kaç tane
buzdolabi = [300, 350, 400, 450, 465, 550, 860]
aylık_kac_satıs = 0
toplam = 0

for satis in buzdolabi:
    if satis >= 400:
        aylık_kac_satıs += 1
print(f"Toplam da {aylık_kac_satıs} ay satılmış")

# 400 adetten fazla satılan buzdolabı toplamları
for satis in buzdolabi:
    if satis >= 400:
        toplam += satis
print(f"Toplam satış: {toplam}")



#özet: girilen sayının basamağını bulmak
sayı_gir = int(input("Basamak değeri hesaplanacak sayıyı girn..."))
basamak = 0

while sayı_gir > 0:
    sayı_gir = sayı_gir // 10
    basamak += 1
print ("Girdiğiniz sayının basamak sayısı:", basamak)


#özet: mevcut yılı al ve girilen doğum yılına göre bir kişinin ehliyet alıp alamayacağını hesaplayan programı yaz
from datetime import datetime

current_year = datetime.now().year
born_year = int(input("Hangi yılda doğdunuz? "))
result = current_year - born_year
if result < 18:
    print("Ehliyet alamazsın reşit değilsin.")
else:
    print("Ehliyet alabilirsin.")



nick_name = input("isminizi girin  ")
if len(nick_name) > 7:
    print("Kullanıcı adı çok uzun")
else:
    print(f"Kullanıcı adı {nick_name} ve iyi")