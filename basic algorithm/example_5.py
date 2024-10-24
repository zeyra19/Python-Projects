metin = input("Palindrom kontrolü için metin girin:")
ters_metin = metin[::-1]

if metin == ters_metin:
    print("polindrom sayısı")
else:
    print("değil, değil, değil")