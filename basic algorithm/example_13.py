#özet: haftada kaç tane serin, sıcak gün var?
serin_gun  = 0
sıcak_gun = 0

for i in range(1, 10):
    sıcaklık = int(input("hava durumu değerlerini girin: "))
    if sıcaklık < 20:
        serin_gun += 1
        print("serin gün sayısı: ", serin_gun)
    else:
        sıcak_gun += 1
        print("sıcak gün sayısı: ", sıcak_gun)



#özet: Bir şirketteki 4 çalışanın maaşları bir dizi şeklinde verilmiştir.
# 30.000 TL ve 30.000 TL’den yüksek olanlara 10.000 TL, 15.000 TL’den yüksek ve 30.000 TL’den düşük
# olanlara 5.000 TL zam yapılıp maaşların olduğu dizi güncellenecek ve tüm maaşlar yazdırılacaktır.
maaslar = [30000, 12000, 16000, 23000]

for i in range(len(maaslar)):
    if maaslar[i] >= 30000:
        maaslar[i] += 10000

    elif 15000 < maaslar[i] < 30000:
        maaslar[i] += 5000

for maas in maaslar:
    print(f"Güncellenmiş maaşlar {maas}")