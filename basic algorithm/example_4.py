#özet: süre hesaplar
sure = int(input("Kaldığınız süreyi giriniz:"))

if sure <= 10:
    print("ödeyeceğin tutar:", sure * 10)
else:
    print("ödeyeceğin tutar:", sure * 50)


#özet: bir kelimeyi birden fazla kez yazdırır
ifade = input("bir kelime gir 10 kere yazdırayım:")
for i in range(10):
    print(ifade)


#özet: bir sayı veriirm ve faktöriyelini hesaplar
def faktoriyel(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * faktoriyel(n-1)

sayi = 3
sonuc = faktoriyel(sayi)
print(f"{sayi} sayısının faktoriyeli = {sonuc}")



#bu sefer sayıyı kullanıcıdan alarak faktöriyel hesaplıcam
sayi = int(input("Sayı giriniz:"))

def faktoriyel(sayi):
    if sayi == 1 or sayi == 0:
        return 1
    else:
        return sayi * faktoriyel(sayi-1)

print("Girdiğin sayının faktöriyeli", faktoriyel(sayi))


# özet: kullanıcıdan sayı alır ve fibanocci dizisi oluşturur
ilk_sayi = int(input("ilk sayıyı girin"))
ikinci_sayi = int(input("ikinci sayıyı girin"))

fibanocci = [ilk_sayi, ikinci_sayi]
# buraya () bunu ekleyemem o zaman tuple olur ve tuple listesini değiştiremem haliyle append metodunu kullanamam
for i in range(10):
    ilk_sayi, ikinci_sayi = ikinci_sayi, ilk_sayi + ikinci_sayi

    fibanocci.append(ikinci_sayi)
    print(fibanocci)
