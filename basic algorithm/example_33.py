# özet: try except hata bulma.
while True:
    try:
        height = float(input("Enter your height: "))
        break
    except ValueError:
        print("Lütfen sayıyı doğru girin")


while True:
    try:
        weight = float(input("Enter your weight: "))
        break
    except ValueError:
        print("Lütfen sayıyı doğru girin")

print(weight / height ** 2)
