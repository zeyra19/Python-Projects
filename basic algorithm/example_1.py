#özet: bir listedeki sayıları toplar
liste = [19,7,8,2,24]
sonuc = sum(liste)
print(sonuc)


#özet: kullanıcıdan sayı alır ve bunları toplar
kullanici = input('Bir takım sayılar giriniz:')
kullanici_listesi = kullanici.split(',')
sonuc = sum(map(int,kullanici_listesi))
print(sonuc)


#özet: kullanıcıdan sayı alır ve bunları toplar ancak bunu 1 satırda yapar
girilen_sayi = sum(map(int, input('Bir takım sayı giriniz:').split(',')))
print(girilen_sayi)
