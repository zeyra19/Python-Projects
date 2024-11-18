#özet: isalnum, isalpha, isasci farkını öğren
kelime_gir = input("Kelime gir isalpha mı isalnum mu bulayım")

if kelime_gir.isalpha():
    print("Bu bir isalpha yani yalnızca harflerden oluşuyo", kelime_gir)
elif kelime_gir.isalnum():
    print("Bu bir isalnum yani harf ve 1-9", kelime_gir)
elif kelime_gir.isascii():
    print("Bu bir asci yani harf, 1-9 ve semboller", kelime_gir)
else:
    print("Bu kelime bişi değil")


#özet: kullanıcıdan iki input al ve listeye ata, sonra iki listeyi birleştir
liste_1 = input("bişiler..").split()
liste_2 = input("bişiler 2..").split()
birles = list(zip(liste_1, liste_2))
print(birles)

#özet: iki listedeki elemanları birleştir
liste_1 = ["zehra", "oğulcan", "nuri"]
liste_2 = [1, 2, 3]
sonuc = zip(liste_1, liste_2)
print(list(sonuc))


#özet: map'i kullan
numbers = [2, 4, 6, 8]


def add_numbers(numbers):
    return numbers + 30

result = map(add_numbers, numbers)
print(list(result))


#özet: sayıların küpünü bul, lambda ve map kullan
# lamda: ilk yapacağımız işlem ikinci parametre
numbers = [2, 4, 6, 8]

print(list(map(lambda x: x**3, numbers)))


#özet: iki sayı listen olsun o listelerin içinde en büyüğünü bulup birleştirebilsin
numbers = [2, 4, 6, 8]
numbers_2 = [5, 9, 3, 7]

# 2 büyükse 5 den ikiyi dön değilse beşi dön
def max_number(x, y):
    if x > y:
        return x
    return y

# map de ilk fonksiyon sonra fonksyon çözsün diye parametreler
result = map(max_number, numbers, numbers_2)
print(list(result))