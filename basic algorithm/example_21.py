#özet: ekok bul
import math

def ekok_lcm(a, b):
    return math.lcm(a, b)

print(ekok_lcm(20,25))

#özet: ebob bul

def ebob_gcd(a, b):
    return math.gcd(a, b)

print(ebob_gcd(5, 20))


#özet: asal sayı kontrolü
enter_number = int(input("Bir sayı gir: "))

if enter_number > 1:
    if enter_number == 2:
        print("En küçük aal sayıyı girdin :)")
    for i in range(2, enter_number):
        if enter_number % i == 0:
            print("Girilen sayı asal sayı değil")
            break
        else:
            print("Asal sayıı")
            break
else:
    print("Düzgün sayı gir")


#özet: kriter seçme
benchmarks = [
    "Pasaportun var mı?",
    "Seyahat etmeyi seviyor musun?",
    "Bu işte 4+ yıl deneyimin var mı?",
    "Bilgisayar bölümlerinden mezun musun?"
]

answer = int(input("Kaç kritere sahipsiniz? (örnek: 1 2 3): "))

if answer <= 2:
    print("Yeterli kriterleri sağlamıyorsunuz")
elif answer > 4:
    print("Böyle bir koşul sağlanmıyor")
else:
    print("işe alındınız")