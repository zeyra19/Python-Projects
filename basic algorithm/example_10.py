#özet: haftalık maaşa, mesai saat parasını hesaplayan program yaz.
weekly_salary = 8000
extra_salary = 250
extra_working = int(input("Bu hafta kaç saat çalıştınız? "))

if extra_working == 0:
    print("Maaşınız 8000 TL")
else:
    extra_salary = extra_working * extra_salary
    weekly_salary = weekly_salary + extra_salary
    print("işte maaşın", weekly_salary)



#özet: eşkenar dörtgen mi bak
edge_1 =input("1. Köşeyi girin: ")
edge_2 =input("2. Köşeyi girin: ")
edge_3 =input("3. Köşeyi girin: ")
edge_4 =input("4. Köşeyi girin: ")

if edge_1 == edge_2 == edge_3 == edge_4:
    print("eşkenar")
else:
    print("değil")



#özet: girilen harf "o" olana kadar harfleri ekranda göstersin o yazıldığında bitsin
char_array = []

while True:
    char = input("Bir harf giriniz")
    if char == "o":
        print("yazılması gerekn sayıyı buldun")
    else:
        char_array.append(char)
        print(char_array, "tekrar dene")
