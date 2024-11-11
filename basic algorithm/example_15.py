#özet: dictionaryde ki key ve valueleri yazdıran program
arabalar = {
    "Tesla": "Model Y",
    "Audi": "Quatro",
    "Renault": "Clio"
}
# values
for araba in arabalar.keys():
    print(araba)



#özet: contunie
# contunie koyduğumda sonsuz döngüye girdi
baslangıc = 0
while baslangıc < 10:
    if baslangıc % 2 == 0:
        continue  # koşul sağlanırsa döngüyü başa alır, tekrar tekrar
        baslangıc += 1
    print("if'in içindeyim")

else:
    print("kod dışı")


#özet: break
while True:
    isim = input("İsim girin")
    if isim == 'zehra':
        break  # koşul sağlanırsa döngü sonlanır, koşul sağlanmazsa döngüyü tekrar başa alır
    print(isim)



#özet: list comprehension nedir ?
# liste oluşturmanın daha hızlı ve kolay yoludur
kelimeler = ["python", "django", "php"]
büyük_kelime = [kelime.upper() for kelime in kelimeler]
print(büyük_kelime)

#list comp. sıralaması
# 1 bir ifade tanımla
# 2 bir döngü yaz
# 3 bir koşul oluştur
#Python'da List Comprehension kullanırken listeye eklemek istediğiniz elemanı doğrudan belirtmek zorundasınız.
# Bu sayede Python, oluşturulan yeni listede hangi değerin yer alacağını anlayabilir.
sayilar = [2, 5, 7, 8, 12]
cift_sayilar = [sayi for sayi in sayilar if sayi % 2 == 0]
print(cift_sayilar)