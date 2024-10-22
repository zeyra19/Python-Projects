#özet: listenin en küçük değerini bulmak için ilk önce küçükten büyüğe sıralat
# sonra listenin ilk elemanını yazdır
# liste.sort() ve print(liste[0])
# ya da min max kullan daha işlevseldir
liste = [2, 6, 8, 29]
en_kucuk = max(liste)
print("en küçük sayııuı:", en_kucuk)


#özet: listeden eleman siler
liste = [1, 5, 6, 7, 89998]
del liste[4]
print(liste)


#özet: ders ort 50 den büyükse dersten geçsin
ders1 = int(input("Ders Notunuzu Giriniz:"))

if ders1 >= 50:
    print("geçtin")
else:
    print("kaldın")


#özet: öğrenci notunu kıyaslar
ogrenci1 = int(input("öğr 1 Ders Notunuzu Giriniz:"))
ogrenci2 = int(input("öğr 2 Ders Notunuzu Giriniz:"))

if ogrenci1 > ogrenci2:
    print("öğrenci 1 daha başarılı")
else:
     print("öğrenci 2 daha başarılı")



#özet: sayı çift mi tek mi kontrol eder
sayi = int(input("Sayı Gir Bende Tek Mi Çift Mi Bakayım::"))

if sayi%2 == 0:
    print("çift")
else:
    print("tek")


#özet: girilen sayı pozitif mi negatif mi bulur
sayi = int(input("Herhangi bir sayı girin:"))

if sayi > 0:
    print("Pozitif sayı")
elif sayi == 0:
    print("0'a eşit")
else:
    print("Negatif sayı")


#özet: 1den .....'ya kadar olan sayıları yazdırır
for i in range(1,11):
    print(i)


#özet: kullanıcıdan sayı alır ve arasındaki sayıları ekrana yazdırır
basla = int(input("Başlangıç sayısını girin"))
bitir = int(input("Bitiş sayısını girin"))

for i in range(basla, bitir):
    print(i)