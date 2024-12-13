# #özet: bir listedeki sayıları toplar
# liste = [19,7,8,2,24]
# sonuc = sum(liste)
# print(sonuc)
#
#
# #özet: kullanıcıdan sayı alır ve bunları toplar
# kullanici = input('Bir takım sayılar giriniz:')
# kullanici_listesi = kullanici.split(',')
# sonuc = sum(map(int, kullanici_listesi))
# print(sonuc)
#
#
# #özet: kullanıcıdan sayı alır ve bunları toplar ancak bunu 1 satırda yapar
# girilen_sayi = sum(map(int, input('Bir takım sayı giriniz:').split(',')))
# print(girilen_sayi)
#
#
# #özet: bir dizinin sayı ortalamasını alırken toplam/len
# array = [1, 2, 3, 4, 7]
# print(sum(array) / len(array))
#
#
# #özet: return değerini yakalayana kadar kendini tekrar eder
# def sum_recursive(n):
#     if n == 1:
#         return 1
#     else :
#         return n + sum_recursive(n-1)
#
# print(sum_recursive(5))


# özet: D ifadesini sıfırncı indekse ekledik
liste = ["A", "B", "C"]
liste.insert(0, "D")
print(liste)

# özet: bir kümenin tüm elemanlarının başka bir küme içerisinde yer alıp almadığını kontrol et
# A.issubset(B) ifadesi, küme A'nın tüm elemanlarının küme B içinde olup olmadığını kontrol eder
a = {1, 4, 9}
b = {1, 4, 9, 2, 5, 8}

print(a.issubset(b)) #True
print(b.issubset(a)) #False



#özet: boş bir küme oluştur
# Birleştirme: union()
# Kesişim: intersection()
# Fark: difference()
# Alt küme: issubset()
# Eşitlik: issuperset()

yeni_küme = set()

yeni_küme.add(19)
yeni_küme.add(7)
yeni_küme.add(1)

print(yeni_küme)


#özet: items ile eleman birleştirme
sözlük = {"name": "Zeyra", "age": "19", "address": "Ankara"}
for key, value in sözlük.items():
    print(key, value)

set1 = set([5,7,9])
set2 = set([5,6,7])
print(set1.union(set2))
