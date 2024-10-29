#özet: dairenin çevresini ve alanını hesaplar
yari_cap = int(input("Yarı çap değerini girin:"))
cevre = 3.14 * 2 * yari_cap
alan = 3.14 * yari_cap * yari_cap
print("çevresi:", cevre)
print("alanı:", alan)



#özet: dikdoetgenin alanıın hesaplar
kisa_kenar = int(input("Kısa kenar değerini girin:"))
uzun_kenar = int(input("Uzun kenar değerini girin:"))
dikdortgen_alan = kisa_kenar * uzun_kenar
print("dikdörtgenin alanı:", dikdortgen_alan)



#özet: isalnum() 8 karakterden kısa mı uzun mu baktık
def kontrol(karakter):
    if len(karakter) <= 8:
        return False
    elif karakter.isalpha():
        return True
    else:
        return False

kullanici_adi = input("Kullanıcı adınızı girin")

if kontrol(karakter=kullanici_adi):
    print("Kullanıcı adınız eşsiz")
else:
    print("Kullanıcı adınızda bir hata var")



#özet: kullanıcıdan 6 adet bir sayı alır ve onları toplar
toplam = 0
for i in range(6):
    sayi = int(input("Lütfen 6 adet sayı giriniz: "))
    toplam += sayi
    print(toplam)



#özet: += operatörü kullanmadan
sayi_listesi = input("Toplanmasını istediğiniz sayıları girin: ").split()
sayi_listesi = [int(sayi) for sayi in sayi_listesi]
print(sum(sayi_listesi))
