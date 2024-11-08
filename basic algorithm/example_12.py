#özet: yazı tura atan program
# ilk adım 1 ile 5 arasında rastgele bir tam sayı üretmek(randint)
import random

yazi_tura = random.randint(1, 5)

if yazi_tura == 3:
    print("Yazı geldi...")
else:
    print("Tura geldiiğ..")



#özet: pizza siparişi alan program
kucuk_boy = 50
orta_boy = 55
buyuk_boy = 60
peynir = 20
icecek_fiyat = 20

print("Pizzacıya hoşgeldiniz...")

boyut = input("Boyut seçin S, M, L gibi... ").upper()
extra_peynir = input("Ekstra peynir ister misiniz? 'Evet' veya 'Hayır'. ").lower()
icecek = input("içecek ister misiniz? 'Evet' veya 'Hayır'. ").lower()

toplam = 0

if boyut == "S":
    toplam += kucuk_boy
elif boyut == "M":
    toplam += orta_boy
else:
    toplam += buyuk_boy

if extra_peynir == "evet":
    toplam += peynir

if icecek == "evet":
    toplam += icecek_fiyat


print(f"Hesabınız {toplam} TL tuttu")



#özet: Lunapark bileti satmak
boy = int(input("Boyunuzu girin .."))
yas = int(input("Yaşınızı girin .."))

if boy <= 160 or yas <= 18:
    print("Kriterler tutmuyor bilet satamayız")
else:
    print("buyrun biletiniz iyi eğlenceler")