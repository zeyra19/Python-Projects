metin = input("Palindrom kontrolü için metin girin:")
ters_metin = metin[::-1]

if metin == ters_metin:
    print("polindrom sayısı")
else:
    print("değil, değil, değil")


# özet: kullanıcıdan yıl ve ay alır ve onu ekrana yazdırır
import calendar

yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

print(calendar.month(yy, mm))


# özet: hesap makinesi
sayi_1 = int(input("Hesaplamak istediğiniz ilk sayıyı girin: "))
islem = input("Yapmak istediğiniz işlemin sembolünü girin: ")
sayi_2 = int(input("Hesaplamak istediğiniz ikinci sayıyı girin: "))

çıkarma = sayi_1 - sayi_2
toplama = sayi_1 + sayi_2
bölme = sayi_1 / sayi_2
çarpma = sayi_1 * sayi_2


if islem == "-":
    print(çıkarma)

if islem == "+":
    print(toplama)

if islem == "/":
    print(bölme)

if islem == "*":
    print(çarpma)