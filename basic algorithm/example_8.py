#özet: kullanıcııdan id listesi al unique mi bak
ids = []
for i in range(3):
    ids.append((input("3 Adet ID girin:  ")))

def is_unique(list_: list, raise_exception: bool = False):
    for i in list_:
        if list_.count(i) == 1:
            return True
        else:
            return False

if is_unique(ids, raise_exception=False):
    print("Harika seçim idler eşsiz", ids)
else:
    print("ID'ler eşsiz olmalı..")



#özet: kullanıcıdan sayı al sayının birden ona kadar çarpımını yaz
number = int(input("Enter the number you want to multiply: "))
for i in range(1, 11):
    print(f"{i} x {number} = {i*number}")
    i += 1 # i = i + 1



#özet: bir fonksiyonla dizideki en küçük ve en büyük sayıyı bul
def find_min_and_max_number(array):
    min_number = min(array)
    max_number = max(array)
    return (min_number, max_number)

print("Örnekteki sayıalrdan en büyüğü ve en küçüğü işte bunlar:", find_min_and_max_number([1, 4, 5, 8, 9, 7, -2]))