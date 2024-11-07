#özet: mod al
bölen = int(input("Bölen sayı: "))
bölünen = int(input("Bölünecek sayı: "))
kalan = bölünen % bölen

if bölen & bölünen == 0:
    print("Girilen sayının modunu alamam.")
if kalan == 0:
    print("BU sayıların modu alınmaz.")
else:
    print("işte modu: ", kalan)



#özet: 1 ile 50 arasındaki tek sayıların toplamı ile
# çift sayıların toplamının
# farkının negatif mi, pozitif mi olduğunu bulan program
tek = 0
cift = 0

for i in range(1, 51, 2):
    # 1 ile 51 arasında 2 adım atlayarak gidecek
    tek += i
    cift += (i + 1)

if (tek - cift) < 0:
    print("Negatifmiş")
else:
    print("Pozitifmiş")



#özet: Verilen iki sayının en büyük ortak bölenini (EBOB) ve ekok bulmak
import math

number_1 = int(input("Number 1 değerini giriniz "))
number_2 = int(input("Number 2 değerini giriniz "))

ebob = math.gcd(number_1, number_2)
ekok = (number_1 * number_2) // ebob

print(f"verilen sayının ebobu: {ebob} ve ekoku {ekok}")



# özet: 0’dan 10’a kadar olan sayılarla (10 hariç)
# 1’den 5’e kadar olan sayıların (5 dahil)
# çarpımını ekrana yazdıran program
for i in range(10):
    for j in range(1, 6):
        carp = i * j
        print(f"{i} x {j} = {carp}")

for i in range(10):
    for j in range(1, 5):
        topla = i + j
        print(f"{i} + {j} = {topla}")