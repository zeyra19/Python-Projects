# #özet: mod al
# bölen = int(input("Bölen sayı: "))
# bölünen = int(input("Bölünecek sayı: "))
# kalan = bölünen % bölen
#
# if bölen & bölünen == 0:
#     print("Girilen sayının modunu alamam.")
# if kalan == 0:
#     print("BU sayıların modu alınmaz.")
# else:
#     print("işte modu: ", kalan)


#özet: 1 ile 50 arasındaki tek sayıların toplamı ile çift sayıların toplamının farkının negatif mi, pozitif mi olduğunu bulan program
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