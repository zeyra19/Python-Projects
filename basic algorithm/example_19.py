#özet: (*) *args. sayısı belli olmayan parametreler için, birden fazla parametre alabiirler
def sayı_topla(*sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam

print(sayı_topla(23, 67, 90, 45))
print(sayı_topla(23, 67, 90, 46))

#özet: **kwargs sayısı belli değil ve key, value ilişkisi
def yazdır(**kwargs):
    print(kwargs)

yazdır(
    sayı=1,
    sayı_2=2,
    sayı_3=3
)