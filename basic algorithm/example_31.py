# #örnek: python numpy
import numpy as np

a = np.array([2, 4, 3])
b = np.array([5])
print(a+b)


# özet: listedeki her bir elemana ilk önce for ile sonra map ile 10 ekle
# liste = [3,  5, 9]

# for i in liste:
#     print(i + 10)

# print(list(map(lambda x: x +10, liste)))
# liste diye tanıtalım ilk başta


# özet: filter ile listedeki elemanlar 2 ye bölünüyor mu bak ve ekrana bastır
# liste = [1, 4, 6, 7, 7, 3, 2]

# print(list(map(lambda x: x % 2 == 0, liste)))
# map ile yaparsak bize true, false döner

# print(list(filter(lambda x: x % 2 == 0, liste)))
# filter ile yaparsak bize 2 ye bölünen sayıları döner


# özet: reduce fonksiyonu ile faktöriyel hesaplama yap
# Sonrasında fonksiyondan dönen sonuç ile beraber listenin bir sonraki elemanını tekrar aynı fonksiyona parametre olarak gönderir.
# Bu süreç listede eleman kalmayana kadar devam eder.

# from functools import reduce
#
#
# def carp(a, b):
#     return a * b
#
#
# print(reduce(carp, [3, 4, 5]))
