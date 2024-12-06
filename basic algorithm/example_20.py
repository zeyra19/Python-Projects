#özet: girilen sayının ardındaki saylardan hangisi tam bölen kontrol et
def sayi_bol(x):
    sayı_listesi = []

    for i in range(1, x + 1):
        if x % i == 0:
            sayı_listesi.append(i)
    print(f"{x} sayısına tam bölünen sayılar: {sayı_listesi}")


try:
    sayi_gir = int(input("Sayı girin: "))
    sayi_bol(sayi_gir)
except ValueError:
    print("geçersiz")


#özet: girilen sayıyın ardındaki tüm sayıları topla
def add_numbers(number):
    total = 0
    for i in range(1, number + 1):
        total += i
    return total

enter_number = int(input("sayı girin"))
result = add_numbers(enter_number)
print("sayıların toplamı", result)


#özet: girilen sayının ardındaki tüm sayıları çarp
def multiply_numbers(number):
    carpım = 1
    for i in range(1, number +1):
        carpım *= i
    return carpım

enter_number = int(input("sayı girin"))
result = multiply_numbers(enter_number)
print("sayıların çarpımı", result)