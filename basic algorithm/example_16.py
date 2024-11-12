#özet: banka programı
total = 2000
secim = input("Kartı sokmak için 's', ayrılmak için 'a' giriniz.").lower()
isim = "Zehra Nur"
if secim == "s":
    while True:
        islem = int(input("""
           Yapmak istediğiniz işlemi seçin
           -------------------------------
           1-Para çekme
           2-Para yatırma
           3-Hesap bilgileri
           4-Kart iade
        """))

        if islem == 1:
            cekilecek_tutar = int(input("Çekmek istediğimiz tutarı girin.."))
            if cekilecek_tutar > total:
                print("Çekilecek tutar bakiyeden fazla...")
            else:
                total = total - cekilecek_tutar
                print("Para çekildi mevcut paranız", total)

        if islem == 2:
            yatacak_tutar = int(input("Yatırmak istediğimiz tutarı girin.."))
            total = yatacak_tutar + total
            print("Para yatırıldı mevcut paranız", total)

        if islem == 3:
            print(f"Hesap sahibi {isim} ve toplam parası {total}")

        elif islem == 4:
            print("Kart iade edildi. Çıkış yapılıyor...")
            break
else:
    print("Ayrıldınız, çıkış yapıldı! ")
