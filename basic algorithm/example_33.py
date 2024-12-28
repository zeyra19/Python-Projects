# # özet: try except hata bulma.
# while True:
#     try:
#         height = float(input("Enter your height: "))
#         break
#     except ValueError:
#         print("Lütfen sayıyı doğru girin")
#
#
#
# while True:
#     try:
#         weight = float(input("Enter your weight: "))
#         break
#     except ValueError:
#         print("Lütfen sayıyı doğru girin")
#     finally:
#         print("Bu finally bloğu her zaman çalışır. Try olmazsa excepte atlanır ve finally ne olursa olsun çalışır. "
#               "try çalışsa bile finally yine çalışır.")
#
# print(weight / height ** 2)


# özet: sayı toplayan fonksiyonu yaz. raise ile hata bulma
def sumNumbers(numbers):

    if type(numbers) != list:
        raise TypeError("Typeerror hatası, Paramtere liste objesi olmalı")

    total = 0

    for i in numbers:
        total += i

    return total


print(sumNumbers("fkdkd"))
